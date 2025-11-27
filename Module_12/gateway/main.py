from fastapi import FastAPI, HTTPException, Depends
import httpx
import asyncio
from auth import require_role
from otel import setup_otel
import time
from prometheus_client import start_http_server, Counter, Histogram
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI(title="Gateway API")

setup_otel(app, service_name="gateway")

BOOK_SERVICE_URL = "http://book-service:8000"
REVIEW_SERVICE_URL = "http://review-service:8001"

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency",
    ["endpoint"]
)


@app.get("/")
def root():
    return {"message": "Gateway is running"}


@app.get("/api/books/{book_id}")
async def get_book(
    book_id: int,
    token=Depends(require_role("admin"))
):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BOOK_SERVICE_URL}/api/books/{book_id}")
        except httpx.RequestError:
            raise HTTPException(status_code=502, detail="Сервис недоступен")

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return response.json()


@app.get("/details/{book_id}")
async def get_book_details(
    book_id: int,
    token=Depends(require_role("admin"))
):
    async with httpx.AsyncClient() as client:

        book_task = client.get(f"{BOOK_SERVICE_URL}/api/books/{book_id}")
        review_task = client.get(f"{REVIEW_SERVICE_URL}/api/reviews/{book_id}")

        book_response, review_response = await asyncio.gather(book_task, review_task)

        if book_response.status_code == 404:
            raise HTTPException(status_code=404, detail="Книга не найдена")

        if review_response.status_code == 404:
            reviews = []
        else:
            reviews = review_response.json()

        return {
            "book": book_response.json(),
            "reviews": reviews
        }


@app.post("/book")
async def create_book_proxy(book: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://book-service:8000/book", json=book)
        return response.json()


class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()

        response = await call_next(request)

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path
        ).inc()

        REQUEST_LATENCY.labels(
            endpoint=request.url.path
        ).observe(time.time() - start_time)

        return response


@app.get("/metrics")
async def metrics():
    return Response(generate_latest(),
                    media_type=CONTENT_TYPE_LATEST)


app.add_middleware(PrometheusMiddleware)

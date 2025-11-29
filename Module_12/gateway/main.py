from fastapi import FastAPI, HTTPException, Depends
import httpx
from auth import require_role
from otel import setup_otel
import time

from prometheus_client import Counter, Histogram
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

from breaker import breaker


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


@breaker
def call_book_service_sync(url: str):
    """
    Синхронный вызов GET 
    Если book-service выключен — breaker откроется.
    """
    r = httpx.get(url, timeout=2.0)
    r.raise_for_status()
    return r.json()


@breaker
def call_book_service_post_sync(url: str, body: dict):
    """
    Синхронный POST — тоже под PyBreaker.
    """
    r = httpx.post(url, json=body, timeout=2.0)
    r.raise_for_status()
    return r.json()


@app.get("/")
def root():
    return {"message": "Gateway is running"}


@app.get("/api/books/{book_id}")
async def get_book(book_id: int, token=Depends(require_role("admin"))):

    try:
        data = call_book_service_sync(
            f"{BOOK_SERVICE_URL}/api/books/{book_id}")

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        raise HTTPException(
            status_code=502, detail="Ошибка ответа book_service")

    except Exception:
        raise HTTPException(status_code=502, detail="book_service недоступен")

    return data


@app.get("/details/{book_id}")
async def get_book_details(book_id: int, token=Depends(require_role("admin"))):

    try:
        book_data = call_book_service_sync(
            f"{BOOK_SERVICE_URL}/api/books/{book_id}")

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        raise HTTPException(
            status_code=502, detail="Ошибка ответа book_service")

    except Exception:
        raise HTTPException(status_code=502, detail="book_service недоступен")

    async with httpx.AsyncClient() as client:
        review_r = await client.get(f"{REVIEW_SERVICE_URL}/api/reviews/{book_id}")

    reviews = [] if review_r.status_code == 404 else review_r.json()

    return {
        "book": book_data,
        "reviews": reviews
    }


@app.post("/book")
async def create_book_proxy(book: dict):

    try:
        data = call_book_service_post_sync(f"{BOOK_SERVICE_URL}/book", book)

    except Exception:
        raise HTTPException(status_code=502, detail="book_service недоступен")

    return data


class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()

        response = await call_next(request)

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path
        ).inc()

        REQUEST_LATENCY.labels(
            endpoint=request.url.path
        ).observe(time.time() - start)

        return response


@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


app.add_middleware(PrometheusMiddleware)

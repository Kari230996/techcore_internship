from fastapi import FastAPI, HTTPException, Depends
import httpx
import asyncio
from auth import require_role
from otel import setup_otel


app = FastAPI(title="Gateway API")

setup_otel(app, service_name="gateway")

BOOK_SERVICE_URL = "http://book-service:8000"
REVIEW_SERVICE_URL = "http://review-service:8001"


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

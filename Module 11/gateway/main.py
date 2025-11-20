from fastapi import FastAPI, HTTPException, Depends
import httpx

from auth import require_role

app = FastAPI(title="Gateway API")

BOOK_SERVICE_URL = "http://book-service:8000"


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
            raise HTTPException(
                status_code=502,
                detail="Сервис недоступен"
            )

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return response.json()

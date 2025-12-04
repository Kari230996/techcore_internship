from fastapi import APIRouter, HTTPException
from author_service import AuthorService

router = APIRouter(prefix="/books", tags=["Книги"])
author_service = AuthorService("https://httpbin.org/status")


@router.get("/books/{book_id}")
async def get_books(book_id: int):
    author = await author_service.get_author(503)  # 503 - код ошибки

    return {
        "id": book_id,
        "title": "Асинхронное программирование в Python",
        "author": author["name"],
    }

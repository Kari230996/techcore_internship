from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.books import BookSchema
from app.repositories.book_repository import BookRepository
from app.database import get_db_session

router = APIRouter(prefix="/books", tags=["Книги"])


@router.post("/")
async def create_book(book: BookSchema, db: AsyncSession = Depends(get_db_session)):
    # для теста
    return book


@router.get("/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db_session)):
    book = await BookRepository.get_by_id(book_id)
    if not book:
        return {"error": "Книга не найдена"}
    return book


@router.put("/{books_id}")
async def update_book(books_id: int, new_date: dict, db: AsyncSession = Depends(get_db_session)):
    update_book = await BookRepository.update(books_id, new_date)
    if not update_book:
        return {"error": "Книга не найдена"}
    return {"message": "Книга обновлена", "book": update_book}

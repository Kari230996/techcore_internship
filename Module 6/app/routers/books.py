from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.books import BookSchema
from app.repositories.book_repository import BookRepository
from app.database import get_db_session

router = APIRouter(prefix="/books", tags=["Книги"])


@router.get("/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db_session)):
    book = await BookRepository.get_by_id(book_id)
    if not book:
        return {"error": "Книга не найдена"}
    return book

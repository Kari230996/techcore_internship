from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from schemas.books import BookSchema
from repositories.book_repository import BookRepository
from database import get_db_session


router = APIRouter(prefix="/books", tags=["Книги"])


@router.post("/")
async def create_book(book: BookSchema, db: AsyncSession = Depends(get_db_session)):
    new_book = await BookRepository.create(db, book)
    return {"message": "Книга создана", "book": new_book}


@router.get("/{book_id}")
async def get_book(book_id: int):
    book = await BookRepository.get_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.get("/")
async def get_all_books():
    books = await BookRepository.get_all()
    return books


@router.put("/{book_id}")
async def update_book(book_id: int, book: BookSchema):
    updated = await BookRepository.update(book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"message": "Книга обновлена", "book": updated}


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    deleted = await BookRepository.delete(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"message": "Книга удалена"}

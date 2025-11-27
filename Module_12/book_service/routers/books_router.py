from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db_session
from models import Book, Author
from schemas.books_schemas import BookCreate, BookResponse
from otel_metrics import increment_books_created

router = APIRouter()


@router.post("/books", response_model=BookResponse)
async def create_book(
    book: BookCreate,
    db: AsyncSession = Depends(get_db_session)
):

    result = await db.execute(
        select(Author).where(Author.id == book.author_id)
    )
    author = result.scalar_one_or_none()

    if author is None:
        raise HTTPException(status_code=400, detail="Автор не найден")

    new_book = Book(
        title=book.title,
        year=book.year,
        author_id=book.author_id
    )

    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)

    increment_books_created()

    return new_book


@router.get("/books/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(
        select(Book).where(Book.id == book_id)
    )
    book = result.scalar_one_or_none()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

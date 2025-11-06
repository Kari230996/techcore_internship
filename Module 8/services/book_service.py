import asyncio
from fastapi import HTTPException

from repositories.book_repository import BookRepository

semaphore = asyncio.Semaphore(5) 


class BookService:
    @staticmethod
    async def get_book(book_id: int):
        async with semaphore:
            book = await BookRepository.get_by_id(book_id)
            if not book:
                raise HTTPException(status_code=404, detail="Книга не найдена")
            return book

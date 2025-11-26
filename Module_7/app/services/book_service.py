from http.client import HTTPException
from app.repositories.book_repository import BookRepository


class BookService:
    @staticmethod
    async def get_book(book_id: int):
        book = await BookRepository.get_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        return book

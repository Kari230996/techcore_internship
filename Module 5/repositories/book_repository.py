from sqlalchemy import select, update, delete

from models import Book
from database import async_session_maker


class BookRepository:
    """Репозиторий для работы с таблицей books"""

    @staticmethod
    async def create(book_data):
        async with async_session_maker() as session:
            new_book = Book(**book_data.model_dump())
            session.add(new_book)
            await session.commit()
            await session.refresh(new_book)
            return new_book

    @staticmethod
    async def get_by_id(book_id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(Book).where(Book.id == book_id))
            return result.scalar_one_or_none()

    @staticmethod
    async def get_all():
        async with async_session_maker() as session:
            result = await session.execute(select(Book))
            return result.scalars().all()

    @staticmethod
    async def update(book_id: int, book_data):
        async with async_session_maker() as session:
            result = await session.execute(select(Book).where(Book.id == book_id))
            book = result.scalar_one_or_none()
            if not book:
                return None

            for field, value in book_data.model_dump().items():
                setattr(book, field, value)

            await session.commit()
            await session.refresh(book)

            return book

    @staticmethod
    async def delete(book_id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(Book).where(Book.id == book_id))
            book = result.scalar_one_or_none()
            if not book:
                return None

            await session.delete()
            await session.commit()
            return True

import json
from sqlalchemy import select, update

from app.models import Book
from app.database import async_session_maker
from app.redis_client import redis_client


class BookRepository:

    @staticmethod
    async def get_by_id(book_id: int):
        cache_key = f"book:{book_id}"

        cached_book = await redis_client.get(cache_key)
        if cached_book:
            print("Книга нашлась в кэше! Используем кэш...")
            return json.loads(cached_book)

        print("Книга не нашлась в кэше. Поиск в базе данных...")

        # если нет в кэше - достаем из базы
        async with async_session_maker() as session:
            query = select(Book).where(Book.id == book_id)
            result = await session.execute(query)
            book = result.scalar_one_or_none()

            if book:

                # Сохраняем в кэш
                book_data = {
                    "id": book.id,
                    "title": book.title,
                    "year": book.year,
                    "author_id": book.author_id

                }

                await redis_client.set(cache_key, json.dumps(book_data), ex=300)
                print(f"Книга сохранена в Redis с ключом {cache_key}")
                return book_data if book else None

    async def update(book_id: int, new_data: dict):
        async with async_session_maker() as session:
            query = (
                update(Book)
                .where(Book.id == book_id)
                .values(**new_data)
                .returning(Book)
            )
            result = await session.execute(query)
            await session.commit()

            updated_book = result.scalar_one_or_none()

            if updated_book:
                cache_key = f"book:{book_id}"
                await redis_client.delete(cache_key)
                print(
                    f"Книга обновлена в базе данных и удалена из кэша по ключу {cache_key}")

            return updated_book

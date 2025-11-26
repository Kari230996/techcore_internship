import asyncio
from models import Book, Author   
from database import async_session_maker


async def add_books():
    async with async_session_maker() as session:
        async with session.begin():

            author1 = Author(name="Теодор Драйзер")
            author2 = Author(name="Джейн Остин")

            book1 = Book(title="Финансист", year=1912, author=author1)
            book2 = Book(title="Гордость и предубеждение",
                         year=1813, author=author2)

            session.add_all([author1, author2, book1, book2])

            # искусственная ошибка - чтобы проверить rollback
            raise Exception("Произошла ошибка")

    print("Книги добавлены в базу данных")


if __name__ == "__main__":
    asyncio.run(add_books())

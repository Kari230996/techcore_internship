import asyncio
from sqlalchemy import text

from database import async_session_maker


async def generate_report():
    query = text(
        """
    SELECT a.name AS author_name,
           COUNT(b.id) AS books_count,
           AVG(b.year) AS avg_year
    FROM authors a
    LEFT JOIN books b ON a.id = b.author_id
    GROUP BY a.name
    ORDER BY books_count DESC;
    """)

    async with async_session_maker() as session:
        result = await session.execute(query)
        rows = result.fetchall()

        for row in rows:
            avg_year = int(row.avg_year) if row.avg_year is not None else "—"
            print(
                f"Автор: {row.author_name}, Книг: {row.books_count}, Средний год: {avg_year}")

if __name__ == "__main__":
    asyncio.run(generate_report())

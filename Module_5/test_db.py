import asyncio
from sqlalchemy import text
from database import engine


# Проверка подкючения
async def test_connection():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT version();"))
        version = result.scalar_one()
        print("Подключение успешно! Версия PostgreSQL:", version)

if __name__ == "__main__":
    asyncio.run(test_connection())

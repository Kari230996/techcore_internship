import asyncio
from database import engine
from models import Base


# Для проверки задачи
async def create_tables():
    async with engine.begin() as conn:
        print("Создание таблиц...")
        await conn.run_sync(Base.metadata.create_all)
        print("Готово!")

if __name__ == "__main__":
    asyncio.run(create_tables())

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends

from models import Base


# Настройка AsyncEngine
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/books_db"

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True, )


async_session_maker = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


# Dependency для FastApi
async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

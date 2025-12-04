import os
import httpx
import pytest
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from testcontainers.postgres import PostgresContainer
from unittest.mock import AsyncMock

from main import app
from app.database import get_db_session
from app.models import Base


os.environ["TESTCONTAINERS_RYUK_DISABLED"] = "true"


@pytest.mark.asyncio
async def test_books_e2e(mocker):
    mocker.patch(
        "main.CacheInvalidationService.listen_for_invalidation", return_value=None)

    mocker.patch("app.redis_client.redis_client.get",
                 new_callable=AsyncMock, return_value=None)
    mocker.patch("app.redis_client.redis_client.set",
                 new_callable=AsyncMock, return_value=None)
    mocker.patch("app.redis_client.redis_client.delete",
                 new_callable=AsyncMock, return_value=None)

    with PostgresContainer("postgres:15") as postgres:
        db_url = (
            postgres.get_connection_url()
            .replace("postgresql+psycopg2://", "postgresql+asyncpg://")
            .replace("postgresql://", "postgresql+asyncpg://")
        )

        engine = create_async_engine(db_url, echo=False)

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        async_session_maker = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession)

        async def override_get_db_session():
            async with async_session_maker() as session:
                yield session

        app.dependency_overrides[get_db_session] = override_get_db_session

        # создаём тестового автора
        async with async_session_maker() as session:
            await session.execute(text("INSERT INTO authors (id, name) VALUES (1, 'Test Author')"))
            await session.commit()

        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
            post_response = await ac.post("/books/", json={"title": "Test Book", "year": 2025, "author_id": 1})
            assert post_response.status_code == 200

            created = post_response.json()

            get_response = await ac.get(f"/books/{created['id']}")
            assert get_response.status_code == 200

            fetched = get_response.json()
            assert fetched["title"] == "Test Book"

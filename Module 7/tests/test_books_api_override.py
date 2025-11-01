import pytest
from fastapi.testclient import TestClient

from main import app
from app.database import get_db_session

# Создаём фейковую зависимость


async def fake_db_session():
    yield "fake_db_session"


@pytest.fixture
def client(mocker):
    app.dependency_overrides[get_db_session] = fake_db_session

    mocker.patch(
        "app.routers.books.BookRepository.get_by_id",
        return_value={"id": 1, "title": "Test Book",
                      "year": 2025, "author_id": 1}
    )

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


def test_get_book_with_fake_db(client):
    response = client.get("/books/1")

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["id"] == 1

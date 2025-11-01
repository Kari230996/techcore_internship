from fastapi.testclient import TestClient

from main import app


def test_get_book_success(mocker):
    client = TestClient(app)

    mocker.patch(
        "app.routers.books.BookRepository.get_by_id",
        return_value={"id": 1, "title": "Test Book",
                      "year": 2025, "author_id": 1}
    )

    response = client.get("/books/1")

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["id"] == 1

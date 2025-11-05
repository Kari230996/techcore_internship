from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_create_book_invalid_data():
    response = client.post("/books/", json={"title": 123, "year": 2025})

    assert response.status_code == 422

    data = response.json()
    assert data["detail"][0]["type"] == "string_type"

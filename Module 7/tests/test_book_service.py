import pytest

from app.services.book_service import BookService


# pytest-asyncio
@pytest.mark.asyncio
async def test_get_book_with_mocked_repo(mocker):
    mocked_repo = mocker.patch(
        "app.repositories.book_repository.BookRepository.get_by_id",
        return_value={"id": 1, "title": "Test Book",
                      "year": 2025, "author_id": 1},
    )

    result = await BookService.get_book(1)

    assert result["title"] == "Test Book"
    assert result["year"] == 2025
    assert result["author_id"] == 1

    mocked_repo.assert_called_once_with(1)

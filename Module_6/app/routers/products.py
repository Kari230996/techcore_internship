import asyncio
from fastapi import APIRouter, HTTPException

from app.repositories.book_repository import BookRepository
from app.repositories.review_repository import ReviewRepository

router = APIRouter(prefix="/api/products", tags=["Продукты"])


@router.get("/{product_id}/details")
async def get_product_details(product_id: int):
    """
    Полиглотный эндпоинт:
    - берёт продукт из Postgres/Redis
    - берёт отзывы из MongoDB
    - делает это параллельно

    """
    book_task = BookRepository.get_by_id(product_id)
    review_task = ReviewRepository.get_for_product(product_id)

    book, reviews = await asyncio.gather(book_task, review_task)

    if not book:
        raise HTTPException(status_code=404, detail="Продукт не найден")

    return {
        "product": book,
        "reviews": reviews,
    }

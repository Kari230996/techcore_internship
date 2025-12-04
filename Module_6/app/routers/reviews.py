from fastapi import APIRouter
from app.schemas.reviews import ReviewIn, ReviewOut
from typing import List

from app.mongo_client import reviews_collection

router = APIRouter(prefix="/api", tags=["Отзывы"])


@router.post("/reviews", response_model=ReviewOut)
async def create_review(review: ReviewIn):
    review_dict = review.dict()
    result = await reviews_collection.insert_one(review_dict)
    review_dict["id"] = str(result.inserted_id)
    return review_dict


@router.get("/products/{product_id}/reviews", response_model=List[ReviewOut])
async def get_reviews(product_id: int):
    cursor = reviews_collection.find({"product_id": product_id})
    reviews = []
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        reviews.append(doc)
    return reviews

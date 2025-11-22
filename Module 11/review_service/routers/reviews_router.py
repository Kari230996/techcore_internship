from fastapi import APIRouter
from pymongo import MongoClient

from schemas.reviews_schemas import ReviewCreate

router = APIRouter()

client = MongoClient("mongodb://mongodb:27017")
db = client["reviews_db"]
collection = db["reviews"]


@router.post("/reviews")
def create_review(review: ReviewCreate):
    doc = review.model_dump()
    result = collection.insert_one(doc)
    return {
        "review_id": str(result.inserted_id),
        "book_id": doc["book_id"],
        "text": doc["text"],
        "rating": doc["rating"],
    }


@router.get("/reviews/{book_id}")
def get_reviews(book_id: int):
    reviews = []
    for r in collection.find({"book_id": book_id}):
        reviews.append({
            "review_id": str(r["_id"]),
            "book_id": r["book_id"],
            "text": r["text"],
            "rating": r["rating"]
        })

    return reviews

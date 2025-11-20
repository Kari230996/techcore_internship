from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReviewCreate(BaseModel):
    book_id: int
    text: str
    rating: int


class ReviewResponse(BaseModel):
    review_id: str
    book_id: int
    text: str
    rating: int
    created_at: Optional[datetime] = None

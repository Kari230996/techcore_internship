from pydantic import BaseModel, Field


class ReviewIn(BaseModel):
    product_id: int
    author: str
    text: str
    rating: int = Field(gt=1, le=5, description="Оценка от 1 до 5")


class ReviewOut(ReviewIn):
    id: str

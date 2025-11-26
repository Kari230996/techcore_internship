from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title: str
    year: Optional[int] = None
    author_id: int


class BookResponse(BaseModel):
    id: int
    title: str
    year: Optional[int]
    author_id: int

    class Config:
        orm_mode = True

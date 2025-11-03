from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    year: int | None = None
    author_id: int
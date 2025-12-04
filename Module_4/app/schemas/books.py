from pydantic import BaseModel



class BookSchema(BaseModel):
    title: str
    year: int | None = None
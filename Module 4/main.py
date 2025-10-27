from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class BookSchema(BaseModel):
    title: str
    year: int | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


# "База данных" в памяти
books_db = {}


# CRUD-операции
@app.post("/books")
async def create_book(book: BookSchema):
    book_id = len(books_db) + 1
    books_db[book_id] = book
    return {"message": f"Книга {book.title} создана!"}


@app.get("/books/{book_id}")
async def get_books(book_id: int):
    if book_id not in books_db:
        return HTTPException(status_code=404, detail={"error": "Книга не найдена"})
    return {"id": book_id, "title": books_db[book_id].title,
            "year": books_db[book_id].year}


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: BookSchema):
    if book_id not in books_db:
        return HTTPException(status_code=404, detail={"error": "Книга не найдена"})
    books_db[book_id] = book
    return {"message": f"Книга {book.title} обновлена!"}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    if book_id not in books_db:
        return HTTPException(status_code=404, detail={"error": "Книга не найдена"})
    del books_db[book_id]
    return {"message": f"Книга {book_id} удалена!"}


@app.get("/books")
async def get_all_books():
    return books_db

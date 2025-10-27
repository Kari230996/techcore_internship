import asyncio
from fastapi import HTTPException, Depends, APIRouter

from app.schemas.books import BookSchema

router = APIRouter(prefix="/books", tags=["Книги"])


@router.get("/")
async def root():
    await asyncio.sleep(0.3)
    return {"message": "Hello World"}


# "База данных" в памяти
books_db = {}


# CRUD-операции
@router.post("/books")
async def create_book(book: BookSchema):
    await asyncio.sleep(0.5)
    book_id = len(books_db) + 1
    books_db[book_id] = book
    return {"message": f"Книга {book.title} создана!"}


@router.get("/books/{book_id}")
async def get_books(book_id: int):
    await asyncio.sleep(0.5)
    if book_id not in books_db:
        return HTTPException(status_code=404, detail={"Книга не найдена"})
    return {"id": book_id, "title": books_db[book_id].title,
            "year": books_db[book_id].year}


@router.put("/books/{book_id}")
async def update_book(book_id: int, book: BookSchema):
    await asyncio.sleep(0.5)
    if book_id not in books_db:
        return HTTPException(status_code=404, detail={"Книга не найдена"})
    books_db[book_id] = book
    return {"message": f"Книга {book.title} обновлена!"}


@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    await asyncio.sleep(0.5)
    if book_id not in books_db:
        return HTTPException(status_code=404, detail={"Книга не найдена"})
    del books_db[book_id]
    return {"message": f"Книга {book_id} удалена!"}


@router.get("/books")
async def get_all_books():
    await asyncio.sleep(0.2)
    return books_db


# DI
class Session:
    def __init__(self):
        print("Открываем соединение с базой...")
        self.conntection = "db_connection"

    async def query(self):
        print("Выполняем запрос...")
        await asyncio.sleep(1)
        return "Результат запроса"

    def close(self):
        print("Закрываем соединение...")


async def get_db_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@router.post("/books_di")
async def create_book(book: BookSchema, db: Session = Depends(get_db_session)):
    result = await db.query()
    return {"message": "Книга создана", "result": result}

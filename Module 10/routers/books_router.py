from fastapi import APIRouter, BackgroundTasks
from services.event_service import EventService
from services.book_service import BookService


books_router = APIRouter(
    prefix="/api/books",
    tags=["Книги"]
)


@books_router.get("/{book_id}")
async def get_books(book_id: int, background_tasks: BackgroundTasks):
    book = await BookService().get_book(book_id)

    background_tasks.add_task(EventService().send_book_view_event, book_id)

    return book

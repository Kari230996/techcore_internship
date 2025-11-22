from fastapi import FastAPI
from database import engine
from models import Base

from routers.books_router import router as books_router
from routers.authors_router import router as authors_router

app = FastAPI(title="Book Service")


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(authors_router, prefix="/api")
app.include_router(books_router, prefix="/api")

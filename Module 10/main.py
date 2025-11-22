from fastapi import FastAPI

from init_db import init_db
from routers import books_router

app = FastAPI(
    title="Techcore Internship API",
    version="1.0.0"
)

app.include_router(books_router)


@app.on_event("startup")
async def startup():
    await init_db()

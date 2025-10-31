from fastapi import FastAPI

from app.routers import books, reviews


app = FastAPI(title="TechCore Internship", version="1.0")

app.include_router(books.router)
app.include_router(reviews.router)

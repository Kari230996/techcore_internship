from fastapi import FastAPI

from routers import books


app = FastAPI(title="TechCore Internship", version="1.0")

app.include_router(books.router)

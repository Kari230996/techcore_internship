from fastapi import FastAPI
import asyncio

from app.routers import books, reviews, products, inventory, hello_world
from app.services.cache_service import CacheInvalidationService

app = FastAPI(title="TechCore Internship", version="1.0")

app.include_router(books.router)
app.include_router(reviews.router)
app.include_router(products.router)
app.include_router(inventory.router)
app.include_router(hello_world.router)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(CacheInvalidationService().listen_for_invalidation())
    print("Фоновая задача слушателя Pub/Sub запущена")

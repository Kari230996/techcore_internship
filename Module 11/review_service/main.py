from fastapi import FastAPI
from routers.reviews_router import router as reviews_router

app = FastAPI(title="Review Service")

app.include_router(reviews_router, prefix="/api")

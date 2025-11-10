# app/main.py
from fastapi import FastAPI
from app.core.celery_app import celery_app
from app.redis_client import redis_client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Techcore Internship API")

# CORS - чтобы можно было тестировать из браузера
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Пример маршрута


@app.get("/")
def root():
    return {"message": "🚀 FastAPI + Celery + Redis + RabbitMQ работают!"}




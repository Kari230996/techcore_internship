from fastapi import FastAPI
from database import engine
from models import Base
from otel import setup_otel, setup_metrics

from confluent_kafka import Producer
from opentelemetry.trace import get_current_span
from prometheus_client import make_asgi_app

from logging_config import setup_logging
from routers.books_router import router as books_router
from routers.authors_router import router as authors_router

import json
import os


# ---------------- LOGGING ----------------
logger = setup_logging()

# ---------------- APP ----------------
app = FastAPI(title="Book Service")

# ---------------- APP VERSION ----------------
APP_VERSION = os.getenv("APP_VERSION", "v1")


# ---------------- OTel (ОДИН РАЗ) ----------------
setup_otel(
    app=app,
    engine=engine,
    service_name="book-service"
)

# ---------------- METRICS ----------------
setup_metrics(app)
app.mount("/metrics", make_asgi_app())


# ---------------- VERSIONS ----------------
@app.get("/version")
def version():
    return {"version": APP_VERSION}


# ---------------- KAFKA ----------------
producer = None


def init_kafka():
    """Инициализация Kafka без падения сервиса"""
    global producer

    kafka_bootstrap = os.getenv(
        "KAFKA_BOOTSTRAP_SERVERS",
        "kafka.monitoring:9092"
    )

    try:
        producer = Producer({
            "bootstrap.servers": kafka_bootstrap
        })
        logger.info("Kafka producer initialized")
    except Exception as e:
        producer = None
        logger.warning(f"Kafka unavailable: {e}")


def send_kafka_event(event_data: dict):
    """Отправка события в Kafka (безопасно)"""
    if not producer:
        return

    span = get_current_span()
    span_context = span.get_span_context()

    headers = {}
    if span_context.is_valid:
        trace_id = f"{span_context.trace_id:032x}"
        span_id = f"{span_context.span_id:016x}"
        headers["traceparent"] = f"00-{trace_id}-{span_id}-01"

    try:
        producer.produce(
            topic="book_events",
            value=json.dumps(event_data).encode("utf-8"),
            headers=headers
        )
        producer.flush()
    except Exception as e:
        logger.warning(f"Kafka send failed: {e}")


# ---------------- STARTUP ----------------
@app.on_event("startup")
async def startup_event():
    logger.info("book-service started")

    # DB
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("database tables created")

    init_kafka()


# ---------------- ROUTES ----------------
@app.post("/book")
async def create_book(book: dict):
    logger.info("create_book called", book=book)

    send_kafka_event({
        "event": "book_created",
        "book": book
    })

    return {"status": "ok"}


# ---------------- ROUTERS ----------------
app.include_router(authors_router, prefix="/api")
app.include_router(books_router, prefix="/api")

from fastapi import FastAPI
from database import engine
from models import Base
from otel import setup_otel
from confluent_kafka import Producer
from opentelemetry.trace import get_current_span
from otel import setup_metrics
from prometheus_client import make_asgi_app
from prometheus_client import start_http_server
from logging_config import setup_logging
import json

from routers.books_router import router as books_router
from routers.authors_router import router as authors_router



logger = setup_logging()


start_http_server(8001)

app = FastAPI(title="Book Service")


setup_otel(app=app, engine=engine, service_name="book-service")

reader = setup_metrics(app)
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

producer = Producer({"bootstrap.servers": "kafka:9092"})


def send_kafka_event(event_data):
    span = get_current_span()
    span_context = span.get_span_context()

    headers = {}

    if span_context.is_valid:
        trace_id = f"{span_context.trace_id:032x}"
        span_id = f"{span_context.span_id:016x}"

        headers["traceparent"] = f"00-{trace_id}-{span_id}-01"

    producer.produce(
        topic="book_events",
        value=json.dumps(event_data).encode("utf-8"),
        headers=headers
    )
    producer.flush()


@app.on_event("startup")
async def startup_event():
    logger.info("book-service started")

    setup_otel(app=app, engine=engine, service_name="book-service")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("database tables created")


@app.post("/book")
async def create_book(book: dict):
    logger.info("create_book called", book=book)
    send_kafka_event({"event": "book_created", "book": book})
    return {"status": "ok"}


app.include_router(authors_router, prefix="/api")
app.include_router(books_router, prefix="/api")

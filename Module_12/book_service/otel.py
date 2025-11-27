from opentelemetry import trace, metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.zipkin.json import ZipkinExporter

from opentelemetry.sdk.resources import Resource

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
# from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
# from opentelemetry.instrumentation.celery import CeleryInstrumentor


def setup_otel(app=None, engine=None, service_name="default-service"):
    resource = Resource(attributes={"service.name": service_name})

    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    zipkin_exporter = ZipkinExporter(
        endpoint="http://zipkin:9411/api/v2/spans",
    )

    provider.add_span_processor(BatchSpanProcessor(zipkin_exporter))

    if app:
        FastAPIInstrumentor().instrument_app(app)

    # HTTPXClientInstrumentor().instrument()

    if engine is not None:
        if hasattr(engine, "sync_engine"):
            SQLAlchemyInstrumentor().instrument(engine=engine.sync_engine)
        else:
            print(
                "SQLAlchemy async engine detected, using sync_engine fallback not available")

    # CeleryInstrumentor().instrument()


def setup_metrics(app):
    resource = Resource(attributes={"service.name": "book-service"})

    reader = PrometheusMetricReader()

    provider = MeterProvider(
        metric_readers=[reader],
        resource=resource
    )

    metrics.set_meter_provider(provider)

    meter = metrics.get_meter("book-service-meter")

    # Пример метрики — счетчик созданных книг
    app.book_counter = meter.create_counter(
        name="books_created_total",
        description="Total created books",
        unit="1"
    )

    return reader

from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor


# -------------------------
# TRACING
# -------------------------

from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor


def setup_otel(app=None, engine=None, service_name="book-service"):
    resource = Resource.create({
        "service.name": service_name
    })

    tracer_provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer_provider)

    otlp_exporter = OTLPSpanExporter(
        endpoint="jaeger-collector.monitoring:4317",
        insecure=True,
    )

    tracer_provider.add_span_processor(
        BatchSpanProcessor(otlp_exporter)
    )

    if app:
        FastAPIInstrumentor.instrument_app(app)

    if engine is not None:
        SQLAlchemyInstrumentor().instrument(
            engine=engine.sync_engine
        )


# -------------------------
# METRICS (Prometheus)
# -------------------------

def setup_metrics(app):
    resource = Resource.create({
        "service.name": "fastapi-book-service"
    })

    reader = PrometheusMetricReader()

    meter_provider = MeterProvider(
        metric_readers=[reader],
        resource=resource
    )

    metrics.set_meter_provider(meter_provider)

    meter = metrics.get_meter("book-service-meter")

    app.book_counter = meter.create_counter(
        name="books_created_total",
        description="Total created books",
        unit="1"
    )

    return reader

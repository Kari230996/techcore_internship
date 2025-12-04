from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from prometheus_client import start_http_server


reader = PrometheusMetricReader()

provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)


meter = metrics.get_meter(__name__)


books_created_counter = meter.create_counter(
    name="books_created_total",
    description="Всего создано книг",
)


def increment_books_created():
    books_created_counter.add(1)

from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.zipkin.json import ZipkinExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

import json
import time


resource = Resource(attributes={"service.name": "analytics-worker"})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(
    ZipkinExporter(endpoint="http://zipkin:9411/api/v2/spans")
)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)
propagator = TraceContextTextMapPropagator()


class AnalyticsWorker:
    def __init__(self):
        self.consumer = Consumer({
            "bootstrap.servers": "kafka:9092",
            "group.id": "analytics",
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False,
        })
        self.consumer.subscribe(["book_events"])
        print("AnalyticsWorker слушает топик book_events...")

        self.mongo = MongoClient("mongodb://mongodb:27017/")
        self.collection = self.mongo["books_analytics"]["event"]

    def run(self):
        while True:
            msg = self.consumer.poll(timeout=1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() != KafkaError._PARTITION_EOF:
                    print("Kafka error:", msg.error())
                continue

            headers = dict(msg.headers() or [])
            traceparent = headers.get("traceparent")

            carrier = {"traceparent": traceparent} if traceparent else {}

            ctx = propagator.extract(carrier)

            with tracer.start_as_current_span(
                    "analytics.process",
                    context=ctx) as span:

                span.set_attribute("kafka.partition", msg.partition())
                span.set_attribute("kafka.topic", msg.topic())

                data = json.loads(msg.value().decode())

                with tracer.start_as_current_span("mongo.insert", context=ctx):
                    self.collection.insert_one({
                        "partition": msg.partition(),
                        "data": data,
                        "timestamp": time.time()
                    })

                print("Событие обработано -> MongoDB сохранено")

            self.consumer.commit()


if __name__ == "__main__":
    AnalyticsWorker().run()

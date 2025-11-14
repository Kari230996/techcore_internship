from confluent_kafka import Consumer, KafkaError


class AnalyticsWorker:

    def __init__(self):
        self.consumer = Consumer({
            "bootstrap.servers": "kafka:9092",
            "group.id": "analytics",
            "auto.offset.reset": "earliest",
        })

        self.consumer.subscribe(["book_events"])

        print("AnalyticsWorker готов. Слушает топик book_events...")

    def run(self):
        while True:
            msg = self.consumer.poll(timeout=1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                print(f"Kafka error: {msg.error()}")
                continue

            print(f"Получено сообщение: {msg.value().decode('utf-8')}")


if __name__ == "__main__":
    worker = AnalyticsWorker()
    worker.run()

from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient
import json


class AnalyticsWorker:

    def __init__(self):
        self.consumer = Consumer({
            "bootstrap.servers": "kafka:9092",
            "group.id": "analytics",
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False,
            "enable.auto.offset.store": False,
        })

        self.consumer.subscribe(["book_events"])

        print("AnalyticsWorker готов. Слушает топик book_events...")

        self.mongo = MongoClient("mongodb://mongodb:27017/")
        self.db = self.mongo["books_analytics"]
        self.collection = self.db["event"]

        print("AnalyticsWorker подключился к MongoDB...")

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
            try:
                data = json.loads(msg.value().decode('utf-8'))
                partition = msg.partition()
                print(f"[Partition {partition}] Получено сообщение: {data}")

                self.collection.insert_one({
                    "partition": partition,
                    "data": data
                })
                print("Сообщение сохранено в MongoDB...")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        


if __name__ == "__main__":
    worker = AnalyticsWorker()
    worker.run()

import asyncio
import json
from aiokafka import AIOKafkaConsumer
from motor.motor_asyncio import AsyncIOMotorClient


class AsyncAnalyticsWorker:
    def __init__(self):
        self.kafka_bootstrap = "kafka:9092"
        self.topic = "book_events"
        self.group_id = "analytics_async"

        self.mongo = AsyncIOMotorClient("mongodb://mongodb:27017/")
        self.db = self.mongo["books_analytics"]
        self.collection = self.db["event_astnc"]

    async def run(self):
        consumer = AIOKafkaConsumer(
            self.topic,
            bootstrap_servers=self.kafka_bootstrap,
            group_id=self.group_id,
            auto_offset_reset="earliest",
            enable_auto_commit=False,

        )

        await consumer.start()
        print("AsyncAnalyticsWorker готов. Слушает топик book_events...")

        try:
            async for msg in consumer:
                data = json.loads(msg.value.decode("utf-8"))

                print(
                    f"[Async] Partition: {msg.partition}, Offset: {msg.offset}, Data: {data}"
                )

                await self.collection.insert_one({
                    "partition": msg.partition,
                    "offset": msg.offset,
                    "data": data
                })

                await consumer.commit()
                print("[Async] Сообщение сохранено в MongoDB...")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

        finally:
            await consumer.stop()
            print("AsyncAnalyticsWorker завершил работу...")


if __name__ == "__main__":
    worker = AsyncAnalyticsWorker()
    asyncio.run(worker.run())

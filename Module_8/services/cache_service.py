import asyncio

from redis_client import redis_client


class CacheInvalidationService:
    CHANNEL = "cache:invalidate"

    @classmethod
    async def publish_invalidation(cls, book_id: int):
        """Отправляет сообщение в Redis Pub/Sub"""
        await redis_client.publish(cls.CHANNEL, str(book_id))
        print(f"Отправлено уведомление об инвалидации кэша для book:{book_id}")

    @classmethod
    async def listen_for_invalidation(cls):
        """Фоновая задача - слушает Redis Pub/Sub"""
        pubsub = redis_client.pubsub()
        await pubsub.subscribe(cls.CHANNEL)

        print("Слушаю Pub/Sub для инвалидации кэша...")

        async for message in pubsub.listen():
            if message["type"] == "message":
                book_id = message["data"]
                key = f"book:{book_id}"
                await redis_client.delete(key)
                print(f"Кэш удалён по ключу {key} после уведомления")

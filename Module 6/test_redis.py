import asyncio
from redis import asyncio as aioredis


async def test_redis_conn():
    redis_client = aioredis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True
    )

    try:
        result = await redis_client.ping()
        print("Подключение успешно! Ответ:", result)
    except Exception as e:
        print(f"Произошла ошибка:", e)

    finally:
        await redis_client.close()

if __name__ == "__main__":
    asyncio.run(test_redis_conn())

import os
from redis import asyncio as aioredis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

redis_client = aioredis.Redis(
    host=REDIS_HOST,
    port=6379,
    db=0,
    decode_responses=True
)

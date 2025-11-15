import asyncio
import json
from kafka_client import producer


class EventService:

    @staticmethod
    async def send_book_view_event(book_id: int):
        payload = {
            "book_id": book_id,
            "event_type": "book_view",
        }

        def _send():
            producer.produce(
                topic="book_events",
                value=json.dumps(payload).encode("utf-8")
            )
            producer.flush(1)

        await asyncio.to_thread(_send)

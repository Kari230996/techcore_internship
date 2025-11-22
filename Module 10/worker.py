import faust

app = faust.App(
    "book_events_analytics",
    store="memory://",
    broker='kafka://kafka:9092',
    broker_client_id="faust-worker",
)


class BookEvent(faust.Record):
    event_id: int
    event: str
    title: str


book_events_topic = app.topic(
    "book_events",
    value_type=BookEvent
)


views_table = (
    app.Table(
        "views_windowed_count",
        default=int,
        key_type=int,
        partitions=1,
    )
    .tumbling(
        size=10,
        expires=30
    )
)


@app.agent(book_events_topic)
async def process_book_events(stream):
    async for event in stream:
        views_table[event.event_id] += 1

        count = views_table[event.event_id].now()

        print(
            f"Книга {event.event_id}: {count} просмотров за последние 10 секунд"
        )

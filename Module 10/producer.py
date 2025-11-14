from confluent_kafka import Producer
import time
import json

conf = {
    'bootstrap.servers': 'kafka:9092',
    'client.id': 'docker-producer',
}

producer = Producer(conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Ошибка доставки: {err}")
    else:
        print(
            f"Сообщение доставлено: topic={msg.topic()}, partition={msg.partition()}, offset={msg.offset()}"
        )


print("Producer запущен. Отправляет сообщения в topic 'book_events'...\n")

i = 0

while True:
    i += 1
    data = {
        "event_id": i,
        "event": "book_created",
        "title": f"Test book {i}"
    }

    producer.produce(
        "book_events",
        value=json.dumps(data),
        callback=delivery_report
    )

    producer.poll(0)
    producer.flush()

    print("Отправлено:", data)

    time.sleep(5)

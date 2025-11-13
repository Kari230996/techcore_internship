from confluent_kafka import Producer

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
            f"Успешная доставка. Топик: {msg.topic()}, партиция: {msg.partition()}, оффсет: {msg.offset()}")


producer.produce(
    'test-topic',
    value='Hello, Kafka!',
    callback=delivery_report
)

producer.poll(1)
producer.flush()

print("Producer завершил работу.")

from celery import Celery

app = Celery(
    "worker",
    broker="amqp://guest:guest@rabbitmq_db:5672//",
    backend="redis://redis_db:6379/0"
)

app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)

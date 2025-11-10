from celery import Celery

celery_app = Celery(
    "techcore_tasks",
    broker="amqp://guest:guest@rabbitmq_db:5672//",  # rabbitmq
    backend="redis://redis_db:6379/0",  # redis
    include=["app.worker_service"],

)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True
)

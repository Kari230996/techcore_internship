from celery import Celery
from kombu import Exchange, Queue
from datetime import timedelta


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
    enable_utc=True,
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    task_default_retry_delay=5,
    task_max_retries=3
)

CELERY_TASK_DEFAULT_QUEUE = "orders"
CELERY_TASK_QUEUES = (
    Queue(
        "orders",
        Exchange("orders"),
        routing_key="orders",
        queue_arguments={
            "x-dead-letter-exchange": "orders.dlx",
            "x-dead-letter-routing-key": "orders.dlq",
        },
    ),
    Queue("orders.dlx", Exchange("orders.dlx"), routing_key="orders.dlx"),
)

celery_app.conf.beat_schedule = {
    "nightly_report_every_5_minutes": {
        "task": "nightly_report",
        "schedule": timedelta(minutes=5),

    }
}


celery_app.conf.task_queues = CELERY_TASK_QUEUES
celery_app.conf.task_default_queue = CELERY_TASK_DEFAULT_QUEUE

celery_app.autodiscover_tasks(["app.worker_service"])

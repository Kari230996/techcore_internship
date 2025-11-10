import time
from app.core.celery_app import celery_app


@celery_app.task(name="process_order_task")
def process_order(order_id: int):
    print(f"Начата обработка заказа {order_id}...")
    time.sleep(10)
    print(f"Заказ {order_id} обработан!")
    return {"order_id": order_id, "status": "processed"}


# if __name__ == "__main__":
#     result = process_order.delay(55)
#     print(f"Отправлена задача, ID: {result.id}")

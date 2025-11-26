from datetime import datetime
import time
from app.core.celery_app import celery_app


@celery_app.task(name="process_order_task", bind=True, max_retries=3)
def process_order(self, order_id: int):
    try:
        print(f"Начата обработка заказа {order_id}...")
        # time.sleep(10)
        # print(f"Заказ {order_id} обработан!")
        # return {"order_id": order_id, "status": "processed"}
        raise ConnectionError("БД недоступна")
    except ConnectionError as exc:
        print(f"Произошла ошибка: {exc}. Повторим попытку...")
        raise self.retry(exc=exc, countdown=5)


@celery_app.task(name="nightly_report")
def nightly_report():
    print(f"Выполнен отчет в {datetime.utcnow()}")
    return {"status": "success", "timestamp": str(datetime.utcnow())}


# if __name__ == "__main__":
#     result = process_order.delay(55)
#     print(f"Отправлена задача, ID: {result.id}")

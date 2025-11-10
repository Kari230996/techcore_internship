
from fastapi import FastAPI, status

from app.worker_service import process_order


app = FastAPI(title="Techcore Internship API")


@app.post("/order", status_code=status.HTTP_202_ACCEPTED)
async def create_order(order_id: int):
    task = process_order.delay(order_id)
    return {
        "message": f"Заказ {order_id} отправлен в очередь на обработку.",
        "task_id": task.id,
        "status": "queued"
    }

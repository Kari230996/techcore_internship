
import asyncio
from redis_client import redis_client


class InventoryService:
    @staticmethod
    async def update_inventory(product_id: int, delta: int):
        lock_name = f"inventory_lock:{product_id}"
        lock = redis_client.lock(lock_name, timeout=10)

        try:
            async with lock:
                print(f"🔒 Блокировка получена для product:{product_id}")

                current_stock = await redis_client.get(f"stock:{product_id}")
                current_stock = int(current_stock or 10)  # по умолчанию 10

                new_stock = current_stock + delta
                if new_stock < 0:
                    raise ValueError("Недостаточно товара на складе")

                await redis_client.set(f"stock:{product_id}", new_stock)
                print(f"📦 Товар {product_id}: {current_stock} → {new_stock}")

                await asyncio.sleep(2)

        except Exception as e:
            print(f"Ошибка при обновлении: {e}")
            raise
        finally:
            print(f"Блокировка освобождена для product:{product_id}")

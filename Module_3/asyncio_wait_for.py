import asyncio

async def slow_task():
    print(f"Медленная задача выполняется...")
    try:
        await asyncio.sleep(10)
        print(f"Медленная задача завершена.")
    except asyncio.CancelledError:
        print(f"Медленная задача была отменена.")
        raise
    

async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2)
        print(f"Результат: {result}")
    except TimeoutError:
        print("Время ожидания истекло.")

if __name__ == "__main__":
    asyncio.run(main())
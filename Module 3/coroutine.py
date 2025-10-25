import asyncio

async def fetch_data(num):
    print(f"Начали задачу {num}")
    await asyncio.sleep(1)
    print(f"Задача {num} завершена")

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())

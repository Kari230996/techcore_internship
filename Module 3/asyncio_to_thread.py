import asyncio
import time


async def main():
    print("Начинаем асинхронную задачу...")
    await asyncio.to_thread(time.sleep, 5)

    print("Блокирующий код выполнен (но Event Loop не блокировался)")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import time

async def task1():
    print("Скачиваем картину...")
    await asyncio.sleep(1)
    print("Картина скачана!")

async def task2():
    print("Обрабатываем данные...")
    await asyncio.sleep(2)
    print("Данные обработаны!")

async def task3():
    print("Получаем данные из сети...")
    await asyncio.sleep(3)
    print("Данные получены!")


async def main():
    start = time.perf_counter()

    await asyncio.gather(task1(), task2(), task3())

    end = time.perf_counter()
    print(f"Затрачено времени: {end - start:.2f} секунд")

if __name__ == "__main__":
    asyncio.run(main())




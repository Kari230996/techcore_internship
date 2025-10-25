import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        item = f"Задача {i}"
        await queue.put(item)
        print(f"Producer добавил: {item}")
    await queue.put(None)  


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumer обработал: {item}")
        await asyncio.sleep(2)
    print("Consumer завершил работу.")


async def main():
    queue = asyncio.Queue()

    await asyncio.gather(producer(queue), consumer(queue))


if __name__ == "__main__":
    asyncio.run(main())

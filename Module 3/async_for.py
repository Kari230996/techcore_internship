import asyncio

async def stream_data():
    for data in range(5):
        await asyncio.sleep(1)
        yield f"Данные {data}"


async def main():
    async for data in stream_data():
        print(f"Получено данные: {data}")


if __name__ == "__main__":
    asyncio.run(main())
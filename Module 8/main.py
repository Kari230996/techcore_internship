import asyncio
from author_service import AuthorService


async def main():
    service = AuthorService("https://httpbin.org/status")

    for i in range(6):
        print(f"\n--- Запрос {i + 1} ---")

        result = await service.get_author(503)
        print(result)
        await asyncio.sleep(0.5)
    await service.close()


asyncio.run(main())

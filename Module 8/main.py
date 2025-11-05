import asyncio
from author_service import AuthorService


async def main():
    service = AuthorService("https://httpbin.org/status")
    result = await service.get_author(503)
    print("Результат:", result)
    await service.close()


asyncio.run(main())

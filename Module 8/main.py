import asyncio
from author_service import AuthorService


async def main():
    author_service = AuthorService("https://httpbin.org")
    result = await author_service.get_author("delay/5")
    print(result)
    await author_service.close()

asyncio.run(main())

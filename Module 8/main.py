import asyncio
from author_service import AuthorService


async def main():
    author_service = AuthorService("https://jsonplaceholder.typicode.com")
    author = await author_service.get_author(1)
    print(author)
    await author_service.close()

asyncio.run(main())

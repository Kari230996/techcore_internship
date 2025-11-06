import asyncio
from author_service import AuthorService
from services.book_service import BookService


async def simulate_requests(i):
    print(f"--- Запрос {i} начался ---")
    await BookService.get_book(1)
    print(f"--- Запрос {i} завершился ---")


async def main():
    await asyncio.gather(*(simulate_requests(i) for i in range(1, 11)))

    # service = AuthorService("https://httpbin.org/status")

    # for i in range(6):
    #     print(f"\n--- Запрос {i + 1} ---")

    #     result = await service.get_author(503)
    #     print(result)
    #     await asyncio.sleep(0.5)
    # await service.close()


asyncio.run(main())

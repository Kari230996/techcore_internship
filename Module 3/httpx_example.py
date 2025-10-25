import asyncio
import httpx
import time

async def fetch(client, url, i):
    response = await client.get(url)
    print(f"Запрос {i:03}: статус {response.status_code}")

    return response.status_code

async def main():
    url = "https://httpbin.org/get"
    total_requests = 100

    start = time.perf_counter()

    async with httpx.AsyncClient() as client:
        # создаем 100 задач
        tasks = [fetch(client, url, i) for i in range(1, total_requests + 1)]
        results = await asyncio.gather(*tasks)

    end = time.perf_counter()
    print(f"\n Выполнено {len(results)} запросов за {end - start:.2f} секунд.")

if __name__ == "__main__":
    asyncio.run(main())

        

    
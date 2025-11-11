import asyncio
import aiohttp


async def fetch_author():
    async with aiohttp.ClientSession() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/users/1")
        response.raise_for_status()
        data = await response.json()
        return {"author": data["name"]}


async def fetch_reviews():
    async with aiohttp.ClientSession() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/comments?postId=1")
        response.raise_for_status()
        data = await response.json()
        # первые 3 отзыва
        return {"reviews": [r["email"] for r in data[:3]]}


async def main():
    print("Запрос данных об авторе и отзывах...")

    task1 = fetch_author()
    task2 = fetch_reviews()

    author_data, review_data = await asyncio.gather(task1, task2)

    combined = {**author_data, **review_data}
    print("Результат:", combined)


if __name__ == "__main__":
    asyncio.run(main())

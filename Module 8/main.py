import asyncio
import httpx


async def fetch_author():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/users/1")
        response.raise_for_status()
        return {"author": response.json()["name"]}


async def fetch_reviews():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/comments?postId=1")
        response.raise_for_status()
        # первые 3 отзыва
        return {"reviews": [r["email"] for r in response.json()[:3]]}


async def main():
    print("Запрос данных об авторе и отзывах...")

    task1 = fetch_author()
    task2 = fetch_reviews()

    author_data, review_data = await asyncio.gather(task1, task2)

    combined = {**author_data, **review_data}
    print("Результат:", combined)


if __name__ == "__main__":
    asyncio.run(main())

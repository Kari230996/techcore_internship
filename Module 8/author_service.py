import asyncio
import httpx
import backoff


class AuthorService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=self.base_url)

    @backoff.on_exception(backoff.expo, httpx.RequestError, max_time=3)
    async def _fetch_author(self, code: int):
        response = await self.client.get(f"/{code}")
        response.raise_for_status()
        return response.json()

    async def get_author(self, author_id: int):
        try:
            data = await self._fetch_author(author_id)
            return data
        except httpx.HTTPStatusError as e:
            print(f"Ошибка HTTP: {e.response.status_code}")
            return {"error": f"Ошибка HTTP: {e.response.status_code}"}
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return {"error": f"Произошла ошибка: {e}"}

    async def close(self):
        await self.client.aclose()

import asyncio
import httpx


class AuthorService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=self.base_url)

    async def get_author(self, author_id: int):
        try:
            response = await asyncio.wait_for(
                self.client.get(f"/delay/5"),
                timeout=2.0
            )
            response.raise_for_status()
            return response.json()
        except asyncio.TimeoutError:
            print("Время ожидания истекло.")
            return {"error": "timeout"}
        except httpx.HTTPError as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return {"error": str(e)}

    async def close(self):
        await self.client.aclose()

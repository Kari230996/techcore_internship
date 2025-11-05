import httpx


class AuthorService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=self.base_url)

    async def get_author(self, author_id: int):
        response = await self.client.get(f"/users/{author_id}")
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()

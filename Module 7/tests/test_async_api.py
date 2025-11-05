import pytest
import httpx
from main import app


@pytest.mark.asyncio
async def test_async_get():
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/hello/")

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, World!"

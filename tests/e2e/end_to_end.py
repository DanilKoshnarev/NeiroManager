import pytest
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
async def test_end_to_end():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Отправка запроса
        response = await client.post("/query", json={"prompt": "Hi!", "service": "chatgpt"})
        assert response.status_code == 200
        data = response.json()
        assert "response" in data
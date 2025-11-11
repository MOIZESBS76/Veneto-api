import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.main import app
from httpx import ASGITransport

@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        r = await ac.get("/health")
        assert r.status_code == 200
        assert r.json() == {"status": "ok"}
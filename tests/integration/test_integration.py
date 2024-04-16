import asyncpg
import requests
import pytest
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / 'favourite_service/app'))
sys.path.append(str(BASE_DIR / 'movies_service/app'))

from favourite_service.app.main import service_alive as favourite_service_status
from movies_service.app.main import service_alive as movies_service_status

@pytest.mark.asyncio
async def test_database_connection():
    try:
        connection = await asyncpg.connect("postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/query")
        assert connection
        await connection.close()
    except Exception as e:
        assert False, f"Не удалось подключиться к базе данных: {e}"


@pytest.mark.asyncio
async def test_favourite_service_connection():
    r = await favourite_service_status()
    assert r == {'message': 'service alive'}

@pytest.mark.asyncio
async def test_movies_service_connection():
    r = await movies_service_status()
    assert r == {'message': 'service alive'}
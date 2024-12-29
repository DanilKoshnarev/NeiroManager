import pytest
from cache.redis_cache import RedisCache

@pytest.mark.asyncio
async def test_redis_cache(mocker):
    mock_redis = mocker.AsyncMock()
    redis_cache = RedisCache()
    redis_cache.redis = mock_redis

    # Тест установки кэша
    await redis_cache.set("test_key", "test_value")
    mock_redis.set.assert_called_with("test_key", "test_value", ex=3600)

    # Тест получения из кэша
    mock_redis.get.return_value = b"test_value"
    value = await redis_cache.get("test_key")
    assert value == b"test_value"
import aioredis
from config.settings import REDIS_HOST, REDIS_PORT, CACHE_TTL

class RedisCache:
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")

    async def get(self, key):
        return await self.redis.get(key)

    async def set(self, key, value):
        await self.redis.set(key, value, ex=CACHE_TTL)

    async def close(self):
        await self.redis.close()
from managers.chatgpt_manager import ChatGPTManager
from cache.redis_cache import RedisCache

class Router:
    def __init__(self):
        self.chatgpt = ChatGPTManager()
        self.cache = RedisCache()

    async def route_request(self, prompt, service="chatgpt"):
        cache_key = f"{service}:{prompt}"
        cached_response = await self.cache.get(cache_key)

        if cached_response:
            return {"cached": True, "response": cached_response.decode()}

        if service == "chatgpt":
            response = await self.chatgpt.generate_response(prompt)
        else:
            response = {"error": "Unsupported service"}

        await self.cache.set(cache_key, response)
        return {"cached": False, "response": response}
import pytest
from router.router import Router

@pytest.mark.asyncio
async def test_router_integration(mocker):
    mock_cache = mocker.AsyncMock()
    mock_chatgpt = mocker.AsyncMock()
    router = Router()
    router.cache = mock_cache
    router.chatgpt = mock_chatgpt

    # Кэш существует
    mock_cache.get.return_value = b"cached_response"
    response = await router.route_request("Hi!", "chatgpt")
    assert response == {"cached": True, "response": "cached_response"}

    # Кэш отсутствует
    mock_cache.get.return_value = None
    mock_chatgpt.generate_response.return_value = "Hello!"
    response = await router.route_request("Hi!", "chatgpt")
    assert response == {"cached": False, "response": "Hello!"}
    mock_cache.set.assert_called_with("chatgpt:Hi!", "Hello!")
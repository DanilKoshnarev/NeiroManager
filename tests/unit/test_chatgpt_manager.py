import pytest
from managers.chatgpt_manager import ChatGPTManager

@pytest.mark.asyncio
async def test_chatgpt_manager(mocker):
    mock_openai = mocker.patch("openai.ChatCompletion.acreate")
    mock_openai.return_value = mocker.AsyncMock(choices=[{"message": {"content": "Hello!"}}])

    manager = ChatGPTManager()
    response = await manager.generate_response("Hi!")
    assert response == "Hello!"
    mock_openai.assert_called_once()
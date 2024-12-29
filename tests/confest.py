import pytest
from unittest.mock import AsyncMock

@pytest.fixture
def mocker():
    from unittest.mock import AsyncMock
    return AsyncMock
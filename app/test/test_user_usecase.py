import pytest
from unittest.mock import MagicMock
from use_cases.user_usecase import UserUseCase

@pytest.fixture
def mock_service(monkeypatch):
    usecase = UserUseCase()
    # Mock del servicio
    usecase.service.get_all = MagicMock(return_value=[{"id":1, "username":"test"}])
    usecase.service.get_by_id = MagicMock(return_value={"id":1, "username":"test"})
    usecase.service.create = MagicMock(return_value={"id":2, "username":"nuevo"})
    usecase.service.update = MagicMock(return_value={"id":1, "username":"update"})
    usecase.service.delete = MagicMock(return_value=True)
    return usecase

def test_list_users(mock_service):
    result = mock_service.list_users()
    assert len(result) == 1
    assert result[0]["username"] == "test"

def test_create_user(mock_service):
    data = {"username":"nuevo"}
    result = mock_service.create_user(data)
    assert result["username"] == "nuevo"

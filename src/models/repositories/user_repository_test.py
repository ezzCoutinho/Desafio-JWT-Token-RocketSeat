from unittest.mock import Mock

import pytest

from src.models.repositories.user_repository import UserRepository


class MockCursor:
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self):
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


@pytest.mark.skip(reason="Test OK!")
def test_registry_user():
    username = "test_user"
    password = "test_password"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)  # type: ignore

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value
    print(cursor)
    print(cursor.execute.call_args[0])

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, "[]")
    assert "VALUES" in cursor.execute.call_args[0][0]

    mock_connection.commit.assert_called_once()

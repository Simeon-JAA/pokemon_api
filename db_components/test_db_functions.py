"""Testing file for db_functions"""

from unittest.mock import patch

from db_functions import get_db_connection


@patch("db_functions.connect")
def test_connect_is_called_in_get_db_connection(mock_connect, mock_config_environment):
    """Tests that connect is called in mock_db_connection"""

    mock_connect.return_value = True

    get_db_connection(mock_config_environment)

    assert mock_connect.call_count == 1


@patch("db_functions.connect")
def test_connect_returns_correct_value_in_get_db_connection(mock_connect, mock_config_environment):
    """Tests that connect returns correct value called in mock_db_connection"""

    mock_connect.return_value = "mock_connection"

    result = get_db_connection(mock_config_environment)

    assert result == "mock_connection"

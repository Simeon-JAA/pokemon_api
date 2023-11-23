"""Testing file for load.py"""

from unittest.mock import MagicMock, patch

from load import get_db_connection


@patch("load.connect")
def test_connect_is_called_in_get_db_connection(mock_connect, mock_config_environment):
    """Tests function get_db_connection returns a successful connection"""

    mock_connect.return_value = True

    get_db_connection(mock_config_environment)

    assert mock_connect.call_count == 1

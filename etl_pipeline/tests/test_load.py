"""Testing file for load.py"""

from unittest.mock import MagicMock, patch

from etl_pipeline.etl.load import get_db_connection


@patch("etl_pipeline.etl.load.connect")
def test_connect_is_called_in_get_db_connection(mock_connect, mock_config_environment):
    """Tests function get_db_connection returns a successful connection"""

    mock_connect.return_value = True

    get_db_connection(mock_config_environment)

    assert mock_connect.call_count == 1


@patch("etl_pipeline.etl.load.connect")
def test_connect_returns_the_correct_value(mock_connect, mock_config_environment):
    """Test a successful connection returns the correct value"""

    mock_connect.return_value = "mock_connection"

    result = get_db_connection(mock_config_environment)

    assert result == "mock_connection"

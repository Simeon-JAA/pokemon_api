"""Testing file for db_functions"""

from unittest.mock import patch

from db_functions import get_user_id
from psycopg2.extensions import connection


@patch("db_functions.get_db_connection")
def test_get_db_connection_returns_connection(mock_db_connection):
    """Test for what should be returned given the function get_db_connection is successful"""

    mock_db_connection.return_value = connection

    result = mock_db_connection()

    assert result == connection


@patch("db_functions.get_db_connection")
def test_get_user_id_calls_cursor(mock_db_connection):
    """Tests that a cursor is acquired in the function get_user_id"""

    mock_db_connection.return_value = connection

    get_user_id(mock_db_connection, "fake user_name")

    assert mock_db_connection.cursor.call_count == 1


@patch("db_functions.get_db_connection")
def test_get_user_id_calls_cursor(mock_db_connection):
    """Tests that a cursor is acquired in the function get_user_id"""

    mock_db_connection.return_value = connection

    result = get_user_id(mock_db_connection, "fake user_name")

    assert mock_db_connection.cursor.call_count == 1

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

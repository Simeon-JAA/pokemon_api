"""Testing file for db_queries"""

import pytest

from unittest.mock import patch

from db_components.db_queries import get_db_connection, get_specific_pokemon
from db_components.db_queries import get_pokemon_by_single_type


@patch("db_components.db_queries.connect")
def test_connect_is_called_in_get_db_connection(mock_connect, mock_config_environment):
    """Tests that connect is called in mock_db_connection"""

    mock_connect.return_value = True

    get_db_connection(mock_config_environment)

    assert mock_connect.call_count == 1


@patch("db_components.db_queries.connect")
def test_connect_returns_correct_value_in_get_db_connection(mock_connect, mock_config_environment):
    """Tests that connect returns correct value called in mock_db_connection"""

    mock_connect.return_value = "mock_connection"

    result = get_db_connection(mock_config_environment)

    assert result == "mock_connection"


@patch("db_components.db_queries.connect", side_effect=ConnectionError("mock connection error"))
def test_error_in_get_db_connection_raises_exception(mock_connect, mock_config_environment):
    """Tests exception is raised with connect returning an error  in mock_db_connection"""

    mock_connect.return_value = "mock connection"

    with pytest.raises(Exception):
        get_db_connection(mock_config_environment)


@patch("db_components.db_queries.connect")
@patch("db_components.db_queries.get_all_pokemon_names")
def test_exception_raised_with_pokemon_name_used_not_in_db(mock_connect, mock_get_all_pokemon_names, mock_all_pokemon_names):
    """Tests exception (value error specifically) raised when a pokemon name is used as an argument
    that is not in the database"""

    mock_connect.return_value = "mock_connection"
    mock_get_all_pokemon_names.return_value = mock_all_pokemon_names

    with pytest.raises(ValueError):
        get_specific_pokemon(mock_connect, "not a pokemon name")


@patch("db_components.db_queries.connect")
@patch("db_components.db_queries.get_all_pokemon_types")
def test_exception_raised_with_pokemon_type_used_not_in_db(mock_connect, mock_get_all_pokemon_types, mock_all_pokemon_types):
    """Tests exception raised (Value error) when type is used in argument that does not exist in the database"""

    mock_connect.return_value = "mock_connection"
    mock_get_all_pokemon_types.return_value = mock_all_pokemon_types

    with pytest.raises(ValueError):
        get_pokemon_by_single_type(mock_connect, "not a pokemon type")

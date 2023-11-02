"""Testing file for extract"""

import pytest
from unittest.mock import MagicMock, patch

from extract import api_request_data, get_pokemon_count, get_pokemon_urls


@patch("extract.requests")
def test_api_request_data_404_exception_raised(mock_requests):
    """Tests exception raised for a 404 status code api_request_data"""

    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_requests.get.return_value = mock_response

    with pytest.raises(Exception):
        api_request_data("fake_url")


@patch("extract.requests")
def test_api_request_data_400_exception_raised(mock_requests):
    """Tests exception raised for 400 status code in api_request_data"""

    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_requests.get.return_value = mock_response

    with pytest.raises(Exception):
        api_request_data("fake_url")


@patch("extract.requests")
def test_api_request_data_200_status_code_returns_data(mock_requests, mock_api_json_return_data):
    """Tests data is returned given a 200 status code in api_request_data"""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_json_return_data
    mock_requests.get.return_value = mock_response

    result = api_request_data("fake_url")

    assert result == mock_api_json_return_data


@patch("extract.requests")
def test_get_pokemon_count_successful_status_code_returns_int(mock_requests, mock_api_json_return_data):
    """Tests integer is returned given a successful status code"""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_json_return_data
    mock_requests.get.return_value = mock_response

    result = get_pokemon_count()

    assert isinstance(result, int)


@patch("extract.requests")
def test_get_pokemon_count_successful_status_code_returns_correct_int(mock_requests, mock_api_json_return_data):
    """Tests correct integer is returned given a successful status code"""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_json_return_data
    mock_requests.get.return_value = mock_response

    result = get_pokemon_count()

    assert result == 500


@patch("extract.requests")
def test_get_pokemon_no_count_key_raises_exception(mock_requests, mock_api_json_return_data_no_count_key):
    """Tests exception is raised if 'count' key isn't present in response data"""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_json_return_data_no_count_key
    mock_requests.get.return_value = mock_response

    with pytest.raises(KeyError):
        get_pokemon_count()


@patch("extract.requests")
def test_get_pokemon_count_as_string_works(mock_requests, mock_api_json_return_data_all_strings):
    """Tests if count value is a string, it will be converted to an int"""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_json_return_data_all_strings
    mock_requests.get.return_value = mock_response

    result = get_pokemon_count()

    assert result == 500


@patch("extract.requests")
def test_get_pokemon_urls_status_code_200_returns_list(mock_requests, mock_api_json_return_data):
    """Tests base case for get_pokemon_urls with status code 200 (returns list)"""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_json_return_data
    mock_requests.get.return_value = mock_response

    result = get_pokemon_urls(1234)

    assert isinstance(result, list)


@patch("extract.requests")
def test_get_pokemon_urls_status_code_200_returns_correct_list(mock_requests, mock_api_json_return_data):
    """Tests base case for get_pokemon_urls with status code 200 (returns the correct list)"""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_json_return_data
    mock_requests.get.return_value = mock_response

    result = get_pokemon_urls(1234)

    assert result == [x["url"] for x in mock_api_json_return_data["results"]]


@patch("extract.requests")
def test_get_pokemon_urls_status_code_400_raises_exception(mock_requests, mock_api_json_return_data):
    """Tests exception raised for 400 status code response in get_pokemon_urls"""

    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = mock_api_json_return_data
    mock_requests.get.return_value = mock_response

    with pytest.raises(Exception):
        get_pokemon_urls(1234)


@patch("extract.requests")
def test_get_pokemon_urls_status_code_404_raises_exception(mock_requests, mock_api_json_return_data):
    """Tests exception raised for 404 status code response in get_pokemon_urls"""

    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.json.return_value = mock_api_json_return_data
    mock_requests.get.return_value = mock_response

    with pytest.raises(Exception):
        get_pokemon_urls(1234)

"""Testing file for extract"""

import pytest
from unittest.mock import MagicMock, patch

from extract import api_request_data


@patch("extract.requests")
def test_api_request_404_exception_raised(mock_requests):
    """Tests exception raised for a 404 status code api_request_data"""

    mock_response = MagicMock()
    mock_response.status_code = 404

    mock_requests.get.return_value = mock_response

    with pytest.raises(Exception):
        api_request_data("fake_url")


@patch("extract.requests")
def test_api_request_400_exception_raised(mock_requests):
    """Tests exception raised for 400 status code in api_request_data"""

    mock_response = MagicMock()
    mock_response.status_code = 400

    mock_requests.get.return_value = mock_response

    with pytest.raises(Exception):
        api_request_data("fake_url")


@patch("extract.requests")
def test_api_request_200_status_code_returns_data(mock_requests):
    """Tests data is returned given a 200 status code in api_request_data"""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "pokemon": "i am a pokemon"
    }
    mock_requests.get.return_value = mock_response

    result = api_request_data("fake_url")

    assert result == {"pokemon": "i am a pokemon"}

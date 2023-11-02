"""Contains mocked and fake pytest fixtures"""

import pytest


@pytest.fixture
def mock_api_json_return_data() -> dict:
    """Fakes the api json data that is returned"""

    return {
        "count": 500,
        "results": [
            {"name": "pokemon_1",
             "url": "pokemon_1_url"},
            {"name": "pokemon_2",
             "url": "pokemon_2_url"},
            {"name": "pokemon_3",
             "url": "pokemon_3_url"},
        ]
    }


@pytest.fixture
def mock_api_json_return_data_all_strings() -> dict:
    """Fakes the api json data that is returned all string values"""

    return {
        "count": "500",
        "result": [
            {"name": "pokemon_1",
             "url": "pokemon_1_url"},
            {"name": "pokemon_2",
             "url": "pokemon_2_url"},
            {"name": "pokemon_3",
             "url": "pokemon_3_url"},
        ]
    }


@pytest.fixture
def mock_api_json_return_data_no_count_key() -> dict:
    """Fakes the api json data that is returned with no count key"""

    return {
        "result": [
            {"name": "pokemon_1",
             "url": "pokemon_1_url"},
            {"name": "pokemon_2",
             "url": "pokemon_2_url"},
            {"name": "pokemon_3",
             "url": "pokemon_3_url"},
        ]
    }


@pytest.fixture
def mock_api_json_return_data_single_pokemon() -> dict:
    """Mocks the api json data that is returned for a single pokemon"""

    return {
        "abilities": [],
        "id": 1,
        "height": 400,
        "weight": 400,
        "is_default": True,
        "moves": [],
        "name": "pokemon_name",
        "stats": [],
        "types": []
    }

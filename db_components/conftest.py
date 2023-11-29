"""Conftest file for db_components"""

import pytest


@pytest.fixture
def mock_config_environment() -> dict:
    """Mocks the environment file"""

    return {
        'USER': 'mock_user',
        'PASSWORD': 'mock_password',
        'DBNAME': 'mock_db_name',
        'PORT': 'mock_port',
        'HOST': 'mock_host'
    }


@pytest.fixture
def mock_all_pokemon_nanmes() -> list[str]:
    """Returns mock of mocked pokemon names"""

    return ["mock_pokemon_name_1",
            "mock_pokemon_name_2",
            "mock_pokemon_name_3",
            "mock_pokemon_name_4",
            "mock_pokemon_name_5",
            "mock_pokemon_name_6",
            "mock_pokemon_name_n"
            ]


@pytest.fixture
def mock_all_pokemon_types() -> list[str]:
    """Mocks and returns all types"""

    return [
        "mock_type_1",
        "mock_type_2",
        "mock_type_3",
        "mock_type_4",
        "mock_type_5",
        "mock_type_6",
        "mock_type_n",
    ]

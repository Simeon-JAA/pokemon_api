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

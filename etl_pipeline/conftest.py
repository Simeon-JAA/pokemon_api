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


@pytest.fixture
def mock_extracted_pokemon_data() -> dict:
    """Mocks extracted pokemon data"""

    return {
        "stats": {'hp': 45, 'attack': 49, 'defense': 49,
                  'special-attack': 65, 'special-defense': 65,
                  'speed': 45, 'height': 7, 'weight': 69,
                  'types': ['grass', 'poison']},

        "abilities": [
            {
                'effect_entries': [
                    {'effect': 'mock ability effect (english) 1',
                     'language': {'name': 'en', 'url': 'mock ability language["url"] 1'},
                     'short_effect': 'mock ability short_effect (english) 2'},
                    {'effect': 'mock ability effect (english) 2',
                     'language': {'name': 'en', 'url': 'mock ability language["url"] 2'},
                     'short_effect': 'mock ability short_effect (english) 2'},
                    {'effect': 'mock ability effect (spanish) 3',
                     'language': {'name': 'es', 'url': 'mock ability language["url"] 3'},
                     'short_effect': 'mock ability short_effect (spanish) 3'},
                    {'effect': 'mock ability effect (french) 4',
                     'language': {'name': 'fr', 'url': 'mock ability language["url"] 4'},
                     'short_effect': 'mock ability short_effect (french) 4'},
                    {'effect': 'mock ability effect (chinese) 5',
                     'language': {'name': 'zh', 'url': 'mock ability language["url"] 5'},
                     'short_effect': 'mock ability short_effect (chinese) 5'},
                ],
                'flavor_text_entries': [
                    {'flavor_text': 'mock flavor_text (english) 1',
                     'language': {'name': 'en', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock version_group["name"] (english) 1',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text (english) 2',
                     'language': {'name': 'en', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock version_group["name"] (english) 2',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text (french) 3',
                     'language': {'name': 'fr', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock version_group["name"] (french) 3',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text (spanish) 4',
                     'language': {'name': 'es', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock version_group["name"] (spanish) 4',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text (chinese) 5',
                     'language': {'name': 'zh', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock version_group["name"] (chinese) 5',
                                       'url': 'mock version_group["url"]'}},
                ],
                'names': [
                    {'language': {'name': 'en', 'url': 'mock language["url"] 1'},
                     'name': 'mock ability name (english) 1'},
                    {'language': {'name': 'fr', 'url': 'mock language["url"] 2'},
                     'name': 'mock ability name (french) 2'},
                    {'language': {'name': 'es', 'url': 'mock language["url"] 3'},
                     'name': 'mock ability name (spanish) 3'},
                    {'language': {'name': 'zh', 'url': 'mock language["url"] 4'},
                     'name': 'mock ability name (chinese) 4'}
                ]
            }, {
                'effect_entries': [
                    {'effect': 'mock ability effect 2 (english) 1',
                     'language': {'name': 'en', 'url': 'mock language["url"]'},
                     'short_effect': 'mock short_effect 2 (english) 1'},
                    {'effect': "mock ability effect 2 (english) 2",
                     'language': {'name': 'en', 'url': 'mock language["url"]'},
                     'short_effect': 'mock short_effect 2 (english) 2'},
                    {'effect': "mock ability effect 2 (spanish) 3",
                     'language': {'name': 'es', 'url': 'mock language["url"]'},
                     'short_effect': 'mock short_effect 2 (spanish) 3'},
                    {'effect': "mock ability effect 2 (french) 4",
                     'language': {'name': 'fr', 'url': 'mock language["url"]'},
                     'short_effect': 'mock short_effect 2 (french) 4'},
                    {'effect': "mock ability effect 2 (chinese) 5",
                     'language': {'name': 'zh', 'url': 'mock language["url"]'},
                     'short_effect': 'mock short_effect 2 (chinese) 5'},
                ],
                'flavor_text_entries': [
                    {'flavor_text': 'mock flavor_text 2 (english) 1',
                     'language': {'name': 'en', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock ability version_group 2 (english) 1',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text 2 (english) 2',
                     'language': {'name': 'en', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock ability version_group 2 (english) 2',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text 2 (english) 3',
                     'language': {'name': 'en', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock ability version_group 2 (english) 3',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text 2 (french) 4',
                     'language': {'name': 'fr', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock ability version_group 2 (french) 4',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text 2 (spanish) 5',
                     'language': {'name': 'es', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock ability version_group 2 (spanish) 5',
                                       'url': 'mock version_group["url"]'}},
                    {'flavor_text': 'mock flavor_text 2 (chinese) 6',
                     'language': {'name': 'zh', 'url': 'mock language["url"]'},
                     'version_group': {'name': 'mock ability version_group 2 (chinese) 6',
                                       'url': 'mock version_group["url"]'}}
                ],
                'names': [
                    {'language': {'name': 'en', 'url': 'mock language["url"]'},
                     'name': 'mock ability name 2 (english) 1'},
                    {'language': {'name': 'fr', 'url': 'mock language["url"]'},
                     'name': 'mock ability name 2 (french) 2'},
                    {'language': {'name': 'es', 'url': 'mock language["url"]'},
                     'name': 'mock ability name 2 (spanish) 3'},
                    {'language': {'name': 'zh', 'url': 'mock language["url"]'},
                     'name': 'mock ability name 2 (chinese) 4'},
                ]
            }
        ]
    }


@pytest.fixture
def mock_flavor_text_entries_three_en_two_fr() -> list[dict]:
    """Mocks all flavor text entries for testing"""

    return [
        {'flavor_text': 'example text 1 (english)',
         'language': {'name': 'en', 'url': 'mock language url 1'},
         'version_group': {'name': 'mock pokemon version_group["name"] 1', 'url': 'mock version group url 1'}},
        {'flavor_text': 'example text 2 (english)',
         'language': {'name': 'en', 'url': 'mock language url 2'},
         'version_group': {'name': 'mock pokemon version_group["name"] 2', 'url': 'mock version group url 2'}},
        {'flavor_text': 'example text 3 (english)',
         'language': {'name': 'en', 'url': 'mock language url 3'},
         'version_group': {'name': 'mock pokemon version_group["name"] 3', 'url': 'mock version group url 3'}},
        {'flavor_text': 'example text 4 (not english)',
         'language': {'name': 'fr', 'url': 'mock language url 4'},
         'version_group': {'name': 'mock pokemon version_group["name"] 4', 'url': 'mock version group url 4'}},
        {'flavor_text': 'example text 5 (not english)',
         'language': {'name': 'fr', 'url': 'mock language url 5'},
         'version_group': {'name': 'mock pokemon version_group["name"] 5', 'url': 'mock version group url 5'}},

    ]


@pytest.fixture
def mock_effect_entries_four_en_three_es() -> list[dict]:
    """Mocks pokemon effect entries"""

    return [
        {'effect': 'mock effect (english) 1',
         'language': {'name': 'en', 'url': 'mock language["url"] 1'},
         'short_effect': 'mock short effect (english) 1'},
        {'effect': 'mock effect (english) 2',
         'language': {'name': 'en', 'url': 'mock language["url"] 2'},
         'short_effect': 'mock short effect (english) 2'},
        {'effect': 'mock effect (english) 3',
         'language': {'name': 'en', 'url': 'mock language["url"] 3'},
         'short_effect': 'mock short effect (english) 3'},
        {'effect': 'mock effect (english) 4',
         'language': {'name': 'en', 'url': 'mock language["url"] 4'},
         'short_effect': 'mock short effect (english) 4'},
        {'effect': 'mock effect (spanish) 5',
         'language': {'name': 'es', 'url': 'mock language["url"] 5'},
         'short_effect': 'mock short effect (not english) 5'},
        {'effect': 'mock effect (spanish) 6',
         'language': {'name': 'es', 'url': 'mock language["url"] 6'},
         'short_effect': 'mock short effect (not english) 6'},
        {'effect': 'mock effect (spanish) 7',
         'language': {'name': 'es', 'url': 'mock language["url"] 7'},
         'short_effect': 'mock short effect (not english) 7'},
    ]


@pytest.fixture
def mock_names_en_sp_fr_zh() -> list[dict]:
    """Mocks pokemon ability names"""

    return [
        {'language': {'name': 'en', 'url': 'mock language url'},
         'name': 'mock ability name (english) 1'},
        {'language': {'name': 'fr', 'url': 'mock language url'},
         'name': 'mock ability name (french) 2'},
        {'language': {'name': 'es', 'url': 'mock language url'},
         'name': 'mock ability name (spanish) 3'},
        {'language': {'name': 'zh', 'url': 'mock language url'},
         'name': 'mock ability name (chinese) 4'},
    ]


@pytest.fixture
def mock_config_environemnt() -> dict:
    """Mocks the envioromnent file"""

    return {
        'USER': 'mock_user',
        'PASSWORD': 'mock_password',
        'DB_NAME': 'mock_db_name',
        'PORT': 'mock_port',
        'HOST': 'mock_host'
    }

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

    return {"stats": {'hp': 45, 'attack': 49, 'defense': 49,
                      'special-attack': 65, 'special-defense': 65,
                      'speed': 45, 'height': 7, 'weight': 69,
                      'types': ['grass', 'poison']},
            "abilities": [{'effect_entries':
                           [{'effect': 'When this Pokémon has 1/3 or less of its HP remaining, its grass-type moves inflict 1.5× as much regular damage.',
                            'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                             'short_effect': 'Strengthens grass moves to inflict 1.5× damage at 1/3 max HP or less.'},
                            {'effect': 'Wenn ein Pokémon mit dieser Fähigkeit nur noch 1/3 seiner maximalen hp oder weniger hat, werden all seine grass Attacken verstärkt, so dass sie 1,5× so viel regular damage anrichten wie sonst.',
                             'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'},
                             'short_effect': 'Erhöht den Schaden von grass Attacken um 50% wenn nur noch 1/3 der maximalen hp oder weniger übrig sind.'}],
                           'flavor_text_entries': [{'flavor_text': 'Ups GRASS moves in a pinch.',
                                                    'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'ruby-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/5/'}},
                                                   {'flavor_text': 'Ups GRASS moves in a pinch.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'emerald', 'url': 'https://pokeapi.co/api/v2/version-group/6/'}},
                                                   {'flavor_text': 'Ups GRASS moves in a pinch.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'firered-leafgreen', 'url': 'https://pokeapi.co/api/v2/version-group/7/'}},
                                                   {'flavor_text': 'Powers up Grass-type\nmoves in a pinch.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group':
                                                    {'name': 'diamond-pearl', 'url': 'https://pokeapi.co/api/v2/version-group/8/'}},
                                                   {'flavor_text': 'Powers up Grass-type\nmoves in a pinch.',
                                                    'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'platinum', 'url': 'https://pokeapi.co/api/v2/version-group/9/'}},
                                                   {'flavor_text': 'Powers up Grass-type\nmoves in a pinch.',
                                                    'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'heartgold-soulsilver', 'url': 'https://pokeapi.co/api/v2/version-group/10/'}},
                                                   {'flavor_text': 'Booste les capacités\nPlante en cas de besoin.',
                                                    'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'},
                                                    'version_group': {'name': 'black-white', 'url': 'https://pokeapi.co/api/v2/version-group/11/'}},
                                                   {'flavor_text': 'Powers up Grass-type\nmoves in a pinch.',
                                                       'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                       'version_group': {'name': 'black-white', 'url': 'https://pokeapi.co/api/v2/version-group/11/'}},
                                                   {'flavor_text': 'Powers up Grass-type\nmoves in a pinch.',
                                                    'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'black-2-white-2', 'url': 'https://pokeapi.co/api/v2/version-group/14/'}},
                                                   {'flavor_text': 'ピンチのとき\u3000くさの\nいりょくが\u3000あがる。',
                                                    'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'},
                                                    'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}},
                                                   {'flavor_text': '위급할 때 풀타입의\n위력이 올라간다.',
                                                    'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'},
                                                    'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}},
                                                   {'flavor_text': 'Booste les capacités Plante en\ncas de besoin.',
                                                    'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'},
                                                    'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}},
                                                   {'flavor_text': 'Erhöht in Notfällen die Stärke\nvon Pflanzen-Attacken.',
                                                    'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'},
                                                    'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}},
                                                   {'flavor_text': 'Potencia los ataques de tipo\nPlanta en un apuro.',
                                                    'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'},
                                                    'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}},
                                                   {'flavor_text': 'Quando si è in difficoltà, potenzia\nle mosse di tipo Erba.',
                                                    'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'},
                                                    'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}},
                                                   {'flavor_text': 'Powers up Grass-type moves\nwhen the Pokémon is in trouble.',
                                                    'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}},
                                                   {'flavor_text': 'ピンチのとき\u3000くさの\n威力が\u3000あがる。',
                                                    'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'},
                                                    'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}},
                                                   {'flavor_text': 'ピンチのとき\u3000くさの\nいりょくが\u3000あがる。',
                                                    'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'},
                                                    'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}},
                                                   {'flavor_text': '위급할 때 풀타입의\n위력이 올라간다.',
                                                    'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'},
                                                    'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}},
                                                   {'flavor_text': 'Booste les capacités Plante en\ncas de besoin.',
                                                    'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'},
                                                    'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}},
                                                   {'flavor_text': 'Erhöht in Notfällen die Stärke\nvon Pflanzen-Attacken.',
                                                    'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'},
                                                    'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}},
                                                   {'flavor_text': 'Potencia los ataques de tipo\nPlanta en un apuro.',
                                                    'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'},
                                                    'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}},
                                                   {'flavor_text': 'Quando si è in difficoltà, potenzia  \nle mosse di tipo Erba.',
                                                    'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'},
                                                    'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}},
                                                   {'flavor_text': 'Powers up Grass-type moves\nwhen the Pokémon is in trouble.',
                                                    'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}},
                                                   {'flavor_text': 'ピンチのとき\u3000くさの\n威力が\u3000あがる。',
                                                    'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'},
                                                    'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}},
                                                   {'flavor_text': 'ＨＰが\u3000へったとき\nくさタイプの\u3000わざの\nいりょくが\u3000あがる。',
                                                    'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'HP가 줄었을 때\n풀타입 기술의\n위력이 올라간다.',
                                                    'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'ＨＰ減少的時候，\n草屬性的招式威力會提高。',
                                                    'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'Augmente la puissance des capacités de type Plante\ndu Pokémon quand il a perdu une certaine quantité\nde PV.',
                                                    'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'Erhöht die Stärke von Pflanzen-Attacken,\nwenn die KP auf einen gewissen Wert fallen.',
                                                    'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'Potencia los movimientos de tipo Planta del Pokémon\ncuando le quedan pocos PS.',
                                                    'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'Quando il Pokémon ha pochi PS, la potenza delle\nsue mosse di tipo Erba aumenta.',
                                                       'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'},
                                                       'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'Powers up Grass-type moves when the Pokémon’s\nHP is low.',
                                                    'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'ＨＰが\u3000減ったとき\nくさタイプの\u3000技の\n威力が\u3000上がる。',
                                                    'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'ＨＰ减少的时候，\n草属性的招式威力会提高。',
                                                    'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'},
                                                    'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}},
                                                   {'flavor_text': 'ＨＰが\u3000へったとき\nくさタイプの\u3000わざの\nいりょくが\u3000あがる。',
                                                    'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'},
                                                    'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}},
                                                   {'flavor_text': 'HP가 줄었을 때\n풀타입 기술의\n위력이 올라간다.',
                                                    'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'},
                                                    'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}},
                                                   {'flavor_text': 'ＨＰ減少的時候，\n草屬性的招式威力會提高。',
                                                    'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'},
                                                    'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}},
                                                   {'flavor_text': 'Augmente la puissance des capacités de type Plante\ndu Pokémon quand il a perdu une certaine quantité\nde PV.',
                                                    'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'},
                                                    'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}},
                                                   {'flavor_text': 'Erhöht die Stärke von Pflanzen-Attacken,\nwenn die KP auf einen gewissen Wert fallen.',
                                                       'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'},
                                                       'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}},
                                                   {'flavor_text': 'Potencia los movimientos de tipo Planta del Pokémon\ncuando le quedan pocos PS.', 'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'Quando il Pokémon ha pochi PS, la potenza delle\nsue mosse di tipo Erba aumenta.', 'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'Powers up Grass-type moves when the Pokémon’s\nHP is low.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'ＨＰが\u3000減ったとき\nくさタイプの\u3000技の\n威力が\u3000上がる。', 'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'ＨＰ减少的时候，\n草属性的招式威力会提高。', 'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'ＨＰが\u3000へったとき\nくさタイプの\u3000わざの\nいりょくが\u3000あがる。', 'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'HP가 줄었을 때\n풀타입 기술의\n위력이 올라간다.', 'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'HP減少的時候，\n草屬性的招式威力會提高。', 'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Augmente la puissance des capacités de type Plante\ndu Pokémon quand il a perdu une certaine quantité\nde PV.', 'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Erhöht die Stärke von Pflanzen-Attacken,\nwenn die KP auf einen gewissen Wert fallen.', 'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Potencia los movimientos de tipo Planta del Pokémon\ncuando le quedan pocos PS.', 'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Quando il Pokémon ha pochi PS, la potenza delle\nsue mosse di tipo Erba aumenta.', 'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Powers up Grass-type moves when the Pokémon’s\nHP is low.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}},
                                                   {'flavor_text': 'HP减少的时候，\n草属性的招式威力会提高。', 'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'},
                                                       'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}},
                                                   {'flavor_text': 'ＨＰが\u3000へったとき\nくさタイプの\u3000わざの\nいりょくが\u3000あがる。', 'language': {
                                                       'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'HP가 줄었을 때\n풀타입 기술의\n위력이 올라간다.', 'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'},
                                                       'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'ＨＰ減少的時候，\n草屬性的招式威力會提高。', 'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'},
                                                       'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'Augmente la puissance des capacités de type Plante\ndu Pokémon quand il a perdu une certaine quantité\nde PV.', 'language': {
                                                       'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'Erhöht die Stärke von Pflanzen-Attacken, wenn die KP\nauf einen gewissen Wert fallen.', 'language': {
                                                       'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'Potencia sus movimientos de tipo Planta cuando le\nquedan pocos PS.', 'language': {
                                                       'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'Quando il Pokémon ha pochi PS, la potenza delle\nsue mosse di tipo Erba aumenta.', 'language': {
                                                       'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'Powers up Grass-type moves when the Pokémon’s\nHP is low.', 'language': {
                                                       'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'ＨＰが\u3000減ったとき\nくさタイプの\u3000技の\n威力が\u3000上がる。', 'language': {
                                                       'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}},
                                                   {'flavor_text': 'ＨＰ减少的时候，\n草属性的招式威力会提高。', 'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}], 'names': [{'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'name': 'しんりょく'}, {'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'name': '심록'}, {'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'}, 'name': '茂盛'}, {'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'name': 'Engrais'}, {'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'name': 'Notdünger'}, {'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'name': 'Espesura'}, {'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'name': 'Erbaiuto'}, {'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'name': 'Overgrow'}, {'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'name': 'しんりょく'}, {'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'}, 'name': '茂盛'}]},
                          {'effect_entries': [{'effect': 'Während strong sunlight ist die speed eines Pokémon mit dieser Fähigkeit doppelt so hoch wie normal.\n\nDieser Bonus zählt nicht als stat modifier.', 'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'short_effect': 'Verdoppelt die speed während starkem Sonnenlicht.'}, {'effect': "This Pokémon's Speed is doubled during strong sunlight.\n\nThis bonus does not count as a stat modifier.", 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'short_effect': 'Doubles Speed during strong sunlight.'}],

                           'flavor_text_entries': [{'flavor_text': 'Raises SPEED in sunshine.',
                                                    'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'ruby-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/5/'}}, {'flavor_text': 'Raises SPEED in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'emerald', 'url': 'https://pokeapi.co/api/v2/version-group/6/'}}, {'flavor_text': 'Raises SPEED in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'firered-leafgreen', 'url': 'https://pokeapi.co/api/v2/version-group/7/'}}, {'flavor_text': 'Boosts the Pokémon’s\nSpeed in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'diamond-pearl', 'url': 'https://pokeapi.co/api/v2/version-group/8/'}}, {'flavor_text': 'Boosts the Pokémon’s\nSpeed in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'platinum', 'url': 'https://pokeapi.co/api/v2/version-group/9/'}}, {'flavor_text': 'Boosts the Pokémon’s\nSpeed in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'heartgold-soulsilver', 'url': 'https://pokeapi.co/api/v2/version-group/10/'}}, {'flavor_text': 'Augmente la Vitesse du\nPokémon s’il y a du soleil.', 'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'black-white', 'url': 'https://pokeapi.co/api/v2/version-group/11/'}}, {'flavor_text': 'Boosts the Pokémon’s\nSpeed in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'black-white', 'url': 'https://pokeapi.co/api/v2/version-group/11/'}}, {'flavor_text': 'Boosts the Pokémon’s\nSpeed in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'black-2-white-2', 'url': 'https://pokeapi.co/api/v2/version-group/14/'}}, {'flavor_text': 'はれのとき\u3000すばやさが\nあがる。', 'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}}, {'flavor_text': '맑을 때 스피드가\n올라간다.', 'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}}, {'flavor_text': 'Augmente la Vitesse du\nPokémon s’il y a du soleil.', 'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}}, {'flavor_text': 'Steigert bei Sonnenschein\ndie Initiative.', 'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}}, {'flavor_text': 'Sube la Velocidad cuando hay\nsol.', 'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}}, {'flavor_text': 'Se c’è il sole, la statistica\nVelocità aumenta.', 'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}}, {'flavor_text': 'Boosts the Pokémon’s\nSpeed stat in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}}, {'flavor_text': '晴れのとき\u3000素早さが\nあがる。', 'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'version_group': {'name': 'x-y', 'url': 'https://pokeapi.co/api/v2/version-group/15/'}}, {'flavor_text': 'はれのとき\u3000すばやさが\nあがる。', 'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}}, {'flavor_text': '맑을 때 스피드가\n올라간다.', 'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}}, {'flavor_text': 'Augmente la Vitesse du\nPokémon s’il y a du soleil.', 'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}}, {'flavor_text': 'Steigert bei Sonnenschein\ndie Initiative.', 'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}}, {'flavor_text': 'Sube la Velocidad cuando hay\nsol.', 'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}}, {'flavor_text': 'Se c’è il sole, la statistica\nVelocità aumenta.', 'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}}, {'flavor_text': 'Boosts the Pokémon’s\nSpeed stat in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}}, {'flavor_text': '晴れのとき\u3000素早さが\nあがる。', 'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'version_group': {'name': 'omega-ruby-alpha-sapphire', 'url': 'https://pokeapi.co/api/v2/version-group/16/'}}, {'flavor_text': 'てんきが\u3000はれのとき\nすばやさが\u3000あがる。', 'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': '날씨가 맑을 때\n스피드가 올라간다.', 'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': '天氣為晴朗時，\n速度會提高。', 'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': 'Augmente la Vitesse du Pokémon s’il y a du soleil.', 'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': 'Erhöht bei Sonnenschein die Initiative.', 'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': 'Sube la Velocidad cuando hace sol.', 'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': 'Se la luce del sole è intensa, la Velocità aumenta.', 'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': 'Boosts the Pokémon’s Speed stat in sunshine.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': '天気が\u3000晴れのとき\n素早さが\u3000上がる。', 'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': '晴朗天气时，\n速度会提高。', 'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'}, 'version_group': {'name': 'sun-moon', 'url': 'https://pokeapi.co/api/v2/version-group/17/'}}, {'flavor_text': 'てんきが\u3000はれのとき\nすばやさが\u3000あがる。', 'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': '날씨가 맑을 때\n스피드가 올라간다.', 'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': '天氣為晴朗時，\n速度會提高。', 'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'Augmente la Vitesse du Pokémon s’il y a du soleil.', 'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'Erhöht bei Sonnenschein die Initiative.', 'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'Sube la Velocidad cuando hace sol.', 'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'Se la luce del sole è intensa, la Velocità aumenta.', 'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'Boosts the Pokémon’s Speed stat in harsh sunlight.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': '天気が\u3000晴れのとき\n素早さが\u3000上がる。', 'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': '晴朗天气时，\n速度会提高。', 'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'}, 'version_group': {'name': 'ultra-sun-ultra-moon', 'url': 'https://pokeapi.co/api/v2/version-group/18/'}}, {'flavor_text': 'てんきが\u3000はれのとき\nすばやさが\u3000あがる。', 'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': '날씨가 맑을 때\n스피드가 올라간다.', 'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': '天氣為晴朗時，\n速度會提高。', 'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Augmente la Vitesse du Pokémon s’il y a du soleil.', 'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Erhöht bei Sonnenschein die Initiative.', 'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Sube la Velocidad cuando hace sol.', 'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Se la luce del sole è intensa, la Velocità aumenta.', 'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'Boosts the Pokémon’s Speed stat in harsh sunlight.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': '天気が\u3000晴れのとき\n素早さが\u3000上がる。', 'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': '晴朗天气时，\n速度会提高。', 'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'}, 'version_group': {'name': 'lets-go-pikachu-lets-go-eevee', 'url': 'https://pokeapi.co/api/v2/version-group/19/'}}, {'flavor_text': 'てんきが\u3000はれのとき\nすばやさが\u3000あがる。', 'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': '날씨가 맑을 때\n스피드가 올라간다.', 'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': '天氣為晴朗時，\n速度會提高。', 'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': 'Augmente la Vitesse du Pokémon s’il y a du soleil.', 'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': 'Erhöht bei Sonnenschein die Initiative.', 'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': 'Sube su Velocidad cuando hace sol.', 'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': 'Se la luce del sole è intensa, la Velocità aumenta.', 'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': 'Boosts the Pokémon’s Speed stat in harsh sunlight.', 'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': '天気が\u3000晴れのとき\n素早さが\u3000上がる。', 'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}, {'flavor_text': '晴朗天气时，\n速度会提高。', 'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'}, 'version_group': {'name': 'sword-shield', 'url': 'https://pokeapi.co/api/v2/version-group/20/'}}], 'names': [{'language': {'name': 'ja-Hrkt', 'url': 'https://pokeapi.co/api/v2/language/1/'}, 'name': 'ようりょくそ'}, {'language': {'name': 'ko', 'url': 'https://pokeapi.co/api/v2/language/3/'}, 'name': '엽록소'}, {'language': {'name': 'zh-Hant', 'url': 'https://pokeapi.co/api/v2/language/4/'}, 'name': '葉綠素'}, {'language': {'name': 'fr', 'url': 'https://pokeapi.co/api/v2/language/5/'}, 'name': 'Chlorophylle'}, {'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'}, 'name': 'Chlorophyll'}, {'language': {'name': 'es', 'url': 'https://pokeapi.co/api/v2/language/7/'}, 'name': 'Clorofila'}, {'language': {'name': 'it', 'url': 'https://pokeapi.co/api/v2/language/8/'}, 'name': 'Clorofilla'}, {'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'}, 'name': 'Chlorophyll'}, {'language': {'name': 'ja', 'url': 'https://pokeapi.co/api/v2/language/11/'}, 'name': 'ようりょくそ'}, {'language': {'name': 'zh-Hans', 'url': 'https://pokeapi.co/api/v2/language/12/'}, 'name': '叶绿素'}]}]
            }

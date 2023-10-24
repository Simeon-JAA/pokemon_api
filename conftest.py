"""Contains mocked and fake pytest fixtures"""

import pytest


@pytest.fixture
def fake_pokemon_bad_data() -> dict:
    """Returns fake pokemon with missing or incorrect fields"""

    pokemon = {"name": "fake_pokemon"}

    return pokemon


@pytest.fixture
def fake_pokemon_pikachu() -> dict:
    """Returns a fake pikachu pokemon"""

    pokemon = {"name": "pikachu",
               "height": 5,
               "weight": 10,
               "stats": [
                   {
                       "base_stat": 35,
                       "effort": 0,
                       "stat": {
                           "name": "hp",
                           "url": "https://pokeapi.co/api/v2/stat/1/"
                       }
                   },
                   {
                       "base_stat": 55,
                       "effort": 0,
                       "stat": {
                           "name": "attack",
                           "url": "https://pokeapi.co/api/v2/stat/2/"
                       }
                   }, {
                       "base_stat": 40,
                       "effort": 0,
                       "stat": {
                           "name": "defense",
                           "url": "https://pokeapi.co/api/v2/stat/3/"
                       }
                   },
                   {
                       "base_stat": 50,
                       "effort": 0,
                       "stat": {
                           "name": "special-attack",
                           "url": "https://pokeapi.co/api/v2/stat/4/"
                       }
                   },
                   {
                       "base_stat": 50,
                       "effort": 0,
                       "stat": {
                           "name": "special-defense",
                           "url": "https://pokeapi.co/api/v2/stat/5/"
                       }
                   },
                   {
                       "base_stat": 90,
                       "effort": 2,
                       "stat": {
                           "name": "speed",
                           "url": "https://pokeapi.co/api/v2/stat/6/"
                       }
                   }
               ]
               }

    return pokemon


@pytest.fixture
def fake_pokemon_pikachu_bad_stats() -> dict:
    """Returns a fake pikachu pokemon with bad stats"""

    pokemon = {"name": "pikachu",
               "height": -5,
               "weight": -500,
               "stats": [
                   {
                       "base_stat": -10,
                       "effort": 0,
                       "stat": {
                           "name": "hp",
                           "url": "https://pokeapi.co/api/v2/stat/1/"
                       }
                   },
                   {
                       "base_stat": -10,
                       "effort": 0,
                       "stat": {
                           "name": "attack",
                           "url": "https://pokeapi.co/api/v2/stat/2/"
                       }
                   }, {
                       "base_stat": -10,
                       "effort": 0,
                       "stat": {
                           "name": "defense",
                           "url": "https://pokeapi.co/api/v2/stat/3/"
                       }
                   },
                   {
                       "base_stat": -10,
                       "effort": 0,
                       "stat": {
                           "name": "special-attack",
                           "url": "https://pokeapi.co/api/v2/stat/4/"
                       }
                   },
                   {
                       "base_stat": -10,
                       "effort": 0,
                       "stat": {
                           "name": "special-defense",
                           "url": "https://pokeapi.co/api/v2/stat/5/"
                       }
                   },
                   {
                       "base_stat": 0,
                       "effort": 2,
                       "stat": {
                           "name": "speed",
                           "url": "https://pokeapi.co/api/v2/stat/6/"
                       }
                   }
               ]
               }

    return pokemon

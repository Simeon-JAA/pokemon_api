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
               "moves": [
                   {
                       "move": {
                           "name": "mega-punch",
                           "url": "https://pokeapi.co/api/v2/move/5/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "fire-punch",
                           "url": "https://pokeapi.co/api/v2/move/7/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "gold-silver",
                                   "url": "https://pokeapi.co/api/v2/version-group/3/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "crystal",
                                   "url": "https://pokeapi.co/api/v2/version-group/4/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "platinum",
                                   "url": "https://pokeapi.co/api/v2/version-group/9/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "black-2-white-2",
                                   "url": "https://pokeapi.co/api/v2/version-group/14/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "omega-ruby-alpha-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/16/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "ultra-sun-ultra-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/18/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "lets-go-pikachu-lets-go-eevee",
                                   "url": "https://pokeapi.co/api/v2/version-group/19/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "scarlet-violet",
                                   "url": "https://pokeapi.co/api/v2/version-group/25/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "thunder-punch",
                           "url": "https://pokeapi.co/api/v2/move/9/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "platinum",
                                   "url": "https://pokeapi.co/api/v2/version-group/9/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "black-2-white-2",
                                   "url": "https://pokeapi.co/api/v2/version-group/14/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "omega-ruby-alpha-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/16/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "ultra-sun-ultra-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/18/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "lets-go-pikachu-lets-go-eevee",
                                   "url": "https://pokeapi.co/api/v2/version-group/19/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "scarlet-violet",
                                   "url": "https://pokeapi.co/api/v2/version-group/25/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "scratch",
                           "url": "https://pokeapi.co/api/v2/move/10/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "gold-silver",
                                   "url": "https://pokeapi.co/api/v2/version-group/3/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "crystal",
                                   "url": "https://pokeapi.co/api/v2/version-group/4/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "ruby-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/5/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "diamond-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/8/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "platinum",
                                   "url": "https://pokeapi.co/api/v2/version-group/9/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "black-white",
                                   "url": "https://pokeapi.co/api/v2/version-group/11/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "colosseum",
                                   "url": "https://pokeapi.co/api/v2/version-group/12/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "xd",
                                   "url": "https://pokeapi.co/api/v2/version-group/13/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "black-2-white-2",
                                   "url": "https://pokeapi.co/api/v2/version-group/14/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "x-y",
                                   "url": "https://pokeapi.co/api/v2/version-group/15/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "omega-ruby-alpha-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/16/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "sun-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/17/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "ultra-sun-ultra-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/18/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "lets-go-pikachu-lets-go-eevee",
                                   "url": "https://pokeapi.co/api/v2/version-group/19/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "brilliant-diamond-and-shining-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/23/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "scarlet-violet",
                                   "url": "https://pokeapi.co/api/v2/version-group/25/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "swords-dance",
                           "url": "https://pokeapi.co/api/v2/move/14/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "ruby-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/5/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "diamond-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/8/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "diamond-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/8/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "platinum",
                                   "url": "https://pokeapi.co/api/v2/version-group/9/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "platinum",
                                   "url": "https://pokeapi.co/api/v2/version-group/9/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "black-white",
                                   "url": "https://pokeapi.co/api/v2/version-group/11/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "black-2-white-2",
                                   "url": "https://pokeapi.co/api/v2/version-group/14/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "x-y",
                                   "url": "https://pokeapi.co/api/v2/version-group/15/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "omega-ruby-alpha-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/16/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "sun-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/17/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "ultra-sun-ultra-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/18/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "brilliant-diamond-and-shining-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/23/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "scarlet-violet",
                                   "url": "https://pokeapi.co/api/v2/version-group/25/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "cut",
                           "url": "https://pokeapi.co/api/v2/move/15/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "gold-silver",
                                   "url": "https://pokeapi.co/api/v2/version-group/3/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "crystal",
                                   "url": "https://pokeapi.co/api/v2/version-group/4/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "ruby-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/5/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "diamond-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/8/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "platinum",
                                   "url": "https://pokeapi.co/api/v2/version-group/9/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "black-white",
                                   "url": "https://pokeapi.co/api/v2/version-group/11/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "colosseum",
                                   "url": "https://pokeapi.co/api/v2/version-group/12/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "xd",
                                   "url": "https://pokeapi.co/api/v2/version-group/13/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "black-2-white-2",
                                   "url": "https://pokeapi.co/api/v2/version-group/14/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "x-y",
                                   "url": "https://pokeapi.co/api/v2/version-group/15/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "omega-ruby-alpha-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/16/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "brilliant-diamond-and-shining-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/23/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "wing-attack",
                           "url": "https://pokeapi.co/api/v2/move/17/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "brilliant-diamond-and-shining-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/23/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "mega-kick",
                           "url": "https://pokeapi.co/api/v2/move/25/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "headbutt",
                           "url": "https://pokeapi.co/api/v2/move/29/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "gold-silver",
                                   "url": "https://pokeapi.co/api/v2/version-group/3/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "crystal",
                                   "url": "https://pokeapi.co/api/v2/version-group/4/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "lets-go-pikachu-lets-go-eevee",
                                   "url": "https://pokeapi.co/api/v2/version-group/19/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "body-slam",
                           "url": "https://pokeapi.co/api/v2/move/34/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "xd",
                                   "url": "https://pokeapi.co/api/v2/version-group/13/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "scarlet-violet",
                                   "url": "https://pokeapi.co/api/v2/version-group/25/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "take-down",
                           "url": "https://pokeapi.co/api/v2/move/36/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "scarlet-violet",
                                   "url": "https://pokeapi.co/api/v2/version-group/25/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "double-edge",
                           "url": "https://pokeapi.co/api/v2/move/38/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "machine",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "tutor",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
                               },
                               "version_group": {
                                   "name": "xd",
                                   "url": "https://pokeapi.co/api/v2/version-group/13/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "leer",
                           "url": "https://pokeapi.co/api/v2/move/43/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 15,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 15,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "bite",
                           "url": "https://pokeapi.co/api/v2/move/44/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "gold-silver",
                                   "url": "https://pokeapi.co/api/v2/version-group/3/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "crystal",
                                   "url": "https://pokeapi.co/api/v2/version-group/4/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "ruby-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/5/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "diamond-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/8/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "platinum",
                                   "url": "https://pokeapi.co/api/v2/version-group/9/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "black-white",
                                   "url": "https://pokeapi.co/api/v2/version-group/11/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "black-2-white-2",
                                   "url": "https://pokeapi.co/api/v2/version-group/14/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "x-y",
                                   "url": "https://pokeapi.co/api/v2/version-group/15/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "omega-ruby-alpha-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/16/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "sun-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/17/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "ultra-sun-ultra-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/18/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "brilliant-diamond-and-shining-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/23/"
                               }
                           },
                           {
                               "level_learned_at": 0,
                               "move_learn_method": {
                                   "name": "egg",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/2/"
                               },
                               "version_group": {
                                   "name": "scarlet-violet",
                                   "url": "https://pokeapi.co/api/v2/version-group/25/"
                               }
                           }
                       ]
                   },
                   {
                       "move": {
                           "name": "growl",
                           "url": "https://pokeapi.co/api/v2/move/45/"
                       },
                       "version_group_details": [
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "red-blue",
                                   "url": "https://pokeapi.co/api/v2/version-group/1/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "yellow",
                                   "url": "https://pokeapi.co/api/v2/version-group/2/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "gold-silver",
                                   "url": "https://pokeapi.co/api/v2/version-group/3/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "crystal",
                                   "url": "https://pokeapi.co/api/v2/version-group/4/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "ruby-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/5/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "emerald",
                                   "url": "https://pokeapi.co/api/v2/version-group/6/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "firered-leafgreen",
                                   "url": "https://pokeapi.co/api/v2/version-group/7/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "diamond-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/8/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "platinum",
                                   "url": "https://pokeapi.co/api/v2/version-group/9/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "heartgold-soulsilver",
                                   "url": "https://pokeapi.co/api/v2/version-group/10/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "black-white",
                                   "url": "https://pokeapi.co/api/v2/version-group/11/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "colosseum",
                                   "url": "https://pokeapi.co/api/v2/version-group/12/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "xd",
                                   "url": "https://pokeapi.co/api/v2/version-group/13/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "black-2-white-2",
                                   "url": "https://pokeapi.co/api/v2/version-group/14/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "x-y",
                                   "url": "https://pokeapi.co/api/v2/version-group/15/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "omega-ruby-alpha-sapphire",
                                   "url": "https://pokeapi.co/api/v2/version-group/16/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "sun-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/17/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "ultra-sun-ultra-moon",
                                   "url": "https://pokeapi.co/api/v2/version-group/18/"
                               }
                           },
                           {
                               "level_learned_at": 4,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "lets-go-pikachu-lets-go-eevee",
                                   "url": "https://pokeapi.co/api/v2/version-group/19/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "sword-shield",
                                   "url": "https://pokeapi.co/api/v2/version-group/20/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "brilliant-diamond-and-shining-pearl",
                                   "url": "https://pokeapi.co/api/v2/version-group/23/"
                               }
                           },
                           {
                               "level_learned_at": 1,
                               "move_learn_method": {
                                   "name": "level-up",
                                   "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                               },
                               "version_group": {
                                   "name": "scarlet-violet",
                                   "url": "https://pokeapi.co/api/v2/version-group/25/"
                               }
                           }
                       ]
                   }
               ],
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


@pytest.fixture
def fake_pokemon_move_version_group_1() -> list:
    """Returns fake version group data"""

    fake_version_group_data = [
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "machine",
                "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
            },
            "version_group": {
                "name": "red-blue",
                "url": "https://pokeapi.co/api/v2/version-group/1/"
            }
        },
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "machine",
                "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
            },
            "version_group": {
                "name": "yellow",
                "url": "https://pokeapi.co/api/v2/version-group/2/"
            }
        },
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "tutor",
                "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
            },
            "version_group": {
                "name": "emerald",
                "url": "https://pokeapi.co/api/v2/version-group/6/"
            }
        },
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "tutor",
                "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
            },
            "version_group": {
                "name": "firered-leafgreen",
                "url": "https://pokeapi.co/api/v2/version-group/7/"
            }
        },
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "machine",
                "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
            },
            "version_group": {
                "name": "sword-shield",
                "url": "https://pokeapi.co/api/v2/version-group/20/"
            }
        }
    ]

    return fake_version_group_data


@pytest.fixture
def fake_pokemon_move_version_group_2() -> list:
    """Returns fake version group data"""

    fake_version_group_data = [
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "machine",
                "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
            },
            "version_group": {
                "name": "red-blue",
                "url": "https://pokeapi.co/api/v2/version-group/1/"
            }
        },
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "machine",
                "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
            },
            "version_group": {
                "name": "diamond-pearl",
                "url": "https://pokeapi.co/api/v2/version-group/2/"
            }
        },
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "tutor",
                "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
            },
            "version_group": {
                "name": "emerald",
                "url": "https://pokeapi.co/api/v2/version-group/6/"
            }
        },
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "tutor",
                "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
            },
            "version_group": {
                "name": "firered-leafgreen",
                "url": "https://pokeapi.co/api/v2/version-group/7/"
            }
        },
        {
            "level_learned_at": 0,
            "move_learn_method": {
                "name": "machine",
                "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
            },
            "version_group": {
                "name": "sword-shield",
                "url": "https://pokeapi.co/api/v2/version-group/20/"
            }
        }
    ]

    return fake_version_group_data

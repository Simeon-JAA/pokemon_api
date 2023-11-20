"""Transform script to filter our only the data required"""


def filter_flavor_text_entries(all_flavor_text_entries: list[dict], language: str = 'en') -> list[dict]:
    """Returns the ability's flavor text for the specified language"""

    flavor_text_keys = {"flavor_text", "version_group"}

    flavor_text_filtered = [dict((k, v) for k, v in x.items()
                                 if k in flavor_text_keys)
                            for x in all_flavor_text_entries
                            if x["language"]["name"] == language.lower()]

    for text in flavor_text_filtered:
        text["version_group"] = text["version_group"].pop("name")

    return flavor_text_filtered


def filter_effect_entries(all_effect_entries: list[dict], language: str = 'en') -> list[dict]:
    """Returns the pokemon effect entries with the chosen filtered language"""

    effect_entry_keys = {"effect", "short_effect"}

    effect_entries_filtered = [dict((k, v) for k, v in x.items()
                                    if k in effect_entry_keys)
                               for x in all_effect_entries
                               if x["language"]["name"] == language.lower()]

    return effect_entries_filtered


def filter_ability_name(all_ability_names: list[dict], language: str = 'en') -> dict:
    """Returns ability name for the specified language provided"""

    desired_ability_keys = {"name"}

    ability_names_filtered = [dict((k, v) for k, v in x.items()
                                   if k in desired_ability_keys)
                              for x in all_ability_names
                              if x["language"]["name"] == language.lower()]

    return ability_names_filtered[0]


def set_abilities_language(pokemon_data: dict, language: str = 'en') -> dict:
    """Returns the pokemon data with abilities section filtered
     to contain entries of the specified language"""

    for ability in pokemon_data["abilities"]:

        flavor_text = ability["flavor_text_entries"]
        ability["flavor_text_entries"] = filter_flavor_text_entries(
            flavor_text, language)

        effect_entries = ability["effect_entries"]
        ability["effect_entries"] = filter_effect_entries(
            effect_entries, language)

        ability_names = ability["names"]
        ability["names"] = filter_ability_name(ability_names, language)

    return pokemon_data


def set_moves_language(pokemon_data: dict, language: str = 'en') -> dict:
    """Returns the pokemon data with moves section filtered
     to contain entries of the specified language"""

    for move in pokemon_data["moves"]:

        flavor_text = move["flavor_text_entries"]
        move["flavor_text_entries"] = filter_flavor_text_entries(
            flavor_text, "en")

        move["damage_class"] = move["damage_class"]["name"]

        names = move["names"]
        move["names"] = filter_ability_name(names, "en")

    return pokemon_data


def transform_pokemon_data(pokemon_data: dict) -> dict:
    """Transforms pokemon data for loading stage"""

    pokemon_data = set_abilities_language(pokemon_data, 'en')

    pokemon_data = set_moves_language(pokemon_data, 'en')

    return pokemon_data


if __name__ == "__main__":

    pass

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


def set_abilities_language(pokemon_data: dict, language: str = 'en') -> dict:
    """Returns the pokemon abilities with the specified language entries only"""

    pokemon_abilities = pokemon_data["abilities"]

    for ability in pokemon_abilities:
        flavor_text = ability["flavor_text_entries"]
        ability["flavor_text_entries"] = filter_flavor_text_entries(
            flavor_text)
    return


def transform_pokemon_data(pokemon_data: dict) -> dict:
    """Transforms pokemon data for loading stage"""

    return pokemon_data


if __name__ == "__main__":

    pass

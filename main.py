"""Runs whole programme"""

import requests


def get_pokemon(pokemon_name: str) -> dict:
    """
    Attempts to make request to the API and if successful, returns
    the pokemon dictionary information for further usage
    """

    try:
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as Err:
        Err("Error: Connection to API unsuccessful!")

    if r.status_code == 404:
        raise Exception(
            f"Error: {pokemon_name} was not found in API!")

    pokemon_data = r.json()

    return pokemon_data


def get_pokemon_dimensions(pokemon_data: dict) -> dict:
    """Returns pokemon dimensions from input data"""

    if not isinstance(pokemon_data, dict):
        raise TypeError("Error: Pokemon data is not in the correct format!")

    if "weight" not in pokemon_data:
        raise KeyError("Error: Pokemon data does not contain 'weight' value!")

    if "height" not in pokemon_data:
        raise KeyError("Error: Pokemon data does not contain 'height' value!")

    if pokemon_data["weight"] <= 0 or pokemon_data["height"] <= 0:
        raise ValueError(
            "Error: Pokemon cannot have a negative weight or height!")

    dimensions_to_return = {}

    dimensions_to_return["weight"] = pokemon_data["weight"]
    dimensions_to_return["height"] = pokemon_data["height"]

    return dimensions_to_return


def check_pokemon_move_version_group(version_group: list, version_name: str, level: int = 0) -> bool:
    """Returns true if the version_name input is in the version_group input"""

    if not isinstance(version_group, list):
        raise TypeError("Error: Pokemon version group is not a list!")

    for version in version_group:
        if version["level_learned_at"] == level and version["version_group"]["name"].lower() == version_name.lower().strip():
            return True

    return False


def get_pokemon_moves(pokemon_data: dict) -> dict:
    """Returns the pokemon's moves from the input dictionary"""

    if not isinstance(pokemon_data, dict):
        raise TypeError("Error: Pokemon data is not in the correct format!")

    if "moves" not in pokemon_data:
        raise KeyError("Error: Pokemon data does not contain any moves!")

    moves_to_return = {}

    for move in pokemon_data["moves"]:
        if check_pokemon_move_version_group(move["version_group_details"], "diamond-pearl"):
            moves_to_return[move["move"]["name"]] = move["move"]["url"]

    return moves_to_return


def get_pokemon_stats(pokemon_data: dict) -> dict:
    """Returns the pokemon's stats from the input dictionary"""

    if not isinstance(pokemon_data, dict):
        raise TypeError("Error: Pokemon data is not in the correct format!")

    if "stats" not in pokemon_data:
        raise ValueError(
            "Error: Pokemon data does not contain 'stats' section!")

    pokemon_stats = pokemon_data["stats"]

    stats_to_return = {}

    for stat in pokemon_stats:

        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]

        if stat_value <= 0:
            raise ValueError(
                f"Error: Pokemon stat ({stat_name}) cannot be equal to or less than 0!")

        stats_to_return[stat_name] = stat_value

    return stats_to_return


# TODO fix ability function
def get_pokemon_abilities(pokemon_data: dict) -> dict:
    """Returns the pokemon's abilities from the input dictionary"""

    if not isinstance(pokemon_data, dict):
        raise TypeError("Error: Pokemon data is not in the correct format!")

    if "abilities" not in pokemon_data:
        raise ValueError(
            "Error: Pokemon data does not contain 'abilities' section!")

    pokemon_abilities = pokemon_data["abilities"]

    abilities_to_return = {}

    for ability in pokemon_abilities:

        ability_url = ability["ability"]["url"]

        try:
            r = requests.get(ability_url)

        except (ConnectionAbortedError, ConnectionError, ConnectionRefusedError) as Err:
            Err("Error: Unsuccessful connection when attempting to get ability information!")

        ability_data = r.json()

        # TODO filter for english
        ability_effect_changes = [x for x in ability_data["effect_changes"]
                                  if x["version_group"]["name"].lower().strip() == "diamond-pearl"]

        ability_effect_entry = [x["effect"] for x in ability_data["effect_entries"]
                                if x["language"]["name"].lower().strip() == "en"][0]

        ability_flavor_text_entry = [x["flavor_text"] for x in ability_data["flavor_text_entries"]
                                     if x["language"]["name"].lower().strip() == "en"
                                     and x["version_group"]["name"].lower().strip() == "diamond-pearl"][0]

        print(ability_effect_changes)

    return abilities_to_return


if __name__ == "__main__":

    print("Search for pokemon")

    while True:

        selected_pokemon = input("Input pokemon:")

        pokemon_data = get_pokemon(selected_pokemon)

        pokemon_stats = get_pokemon_stats(pokemon_data)
        pokemon_moves = get_pokemon_moves(pokemon_data)

        # pokemon_abilities = get_pokemon_abilities(pokemon_data)

        print(pokemon_moves)

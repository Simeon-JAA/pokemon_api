"""Runs whole programme"""

import requests


def get_pokemon(pokemon_name: str) -> dict:
    """
    Attempts to make request to the API and if successful, returns
    the pokemon dictionary information for further usage
    """

    try:
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        pokemon_data = r.json()

    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as Err:
        Err("Error: Connection unsuccessful!")

    return pokemon_data


def get_pokemon_moves(pokemon_data: dict) -> dict:
    """Returns the pokemon's moves from the input dictionary"""

    if not isinstance(pokemon_data, dict):
        raise TypeError("Error: Pokemon data is not in the correct format!")

    if "moves" not in pokemon_data:
        raise ValueError(
            "Error: Pokemon data does not contain 'moves' section!")

    return pokemon_data["moves"]


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


def get_pokemon_stats(pokemon_data: dict) -> dict:
    """Returns the pokemon's abilities from the input dictionary"""

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


# TODO
def get_pokemon_abilities(pokemon_data: dict) -> dict:
    """Returns the pokemon's stats from the input dictionary"""

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

        print(ability_data)
        # TODO filter for english

    return abilities_to_return


if __name__ == "__main__":

    print("Search for pokemon")

    selected_pokemon = input("Input pokemon:")

    pokemon_data = get_pokemon(selected_pokemon)

    # pokemon_stats = get_pokemon_stats(pokemon_data)
    pokemon_abilities = get_pokemon_abilities(pokemon_data)

    # print(pokemon_stats)
    print(pokemon_abilities)

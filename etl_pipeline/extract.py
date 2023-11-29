"""Extract Script: Will extract data from the api"""

import requests


def api_request_data(url: str) -> dict:
    """Attempts to make request to the API and if successful, returns the data"""

    try:
        r = requests.get(url)

        if r.status_code >= 400:
            raise ValueError(f"Error: Problem with provided URL ({url})!")

    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as conn_err:
        conn_err("Error: Connection to API was unsuccessful!")

    data = r.json()

    return data


def get_pokemon_count() -> int:
    """Makes request to the API to get the count of pokemon in the API"""

    url = "https://pokeapi.co/api/v2/pokemon"

    try:
        data = api_request_data(url)

    except:
        Exception("Error: Error making request to the API!")

    if "count" not in data:
        raise KeyError("Error: 'Count' not available in data!")

    pokemon_count = int(data["count"])

    return pokemon_count


def get_pokemon_urls(api_pokemon_count: int) -> list[str]:
    """Returns list of all the pokemon urls to make requests to"""

    api_count_limit_value = api_pokemon_count - 1

    url = f"https://pokeapi.co/api/v2/pokemon?offset=0&limit={api_count_limit_value}"

    pokemon_data_all = api_request_data(url)

    results = pokemon_data_all["results"]

    pokemon_urls = [x["url"] for x in results]

    return pokemon_urls


def get_pokemon_stats(pokemon_data: dict) -> dict:
    """Returns pokemon stats"""

    base_stats = {}

    pokemon_stats_only = pokemon_data["stats"]
    pokemon_types_only = pokemon_data["types"]

    for stat in pokemon_stats_only:

        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        base_stats[stat_name] = stat_value

    pokemon_types = []

    for pokemon_type in pokemon_types_only:
        pokemon_types.append(pokemon_type["type"]["name"])

    pokemon_height = pokemon_data["height"]
    pokemon_weight = pokemon_data["weight"]

    base_stats["height"] = pokemon_height
    base_stats["weight"] = pokemon_weight
    base_stats["types"] = pokemon_types

    return base_stats


def get_pokemon_abilities(pokemon_data: dict) -> list[dict]:
    """Returns the pokemon's abilities"""

    abilities_to_return = []

    desired_ability_keys = {"effect_entries", "flavor_text_entries", "names"}
    pokemon_abilities = pokemon_data["abilities"]

    for ability in pokemon_abilities:

        ability_url = ability["ability"]["url"]
        ability_data = api_request_data(ability_url)

        ability_data_filtered = dict((k, v) for
                                     k, v in ability_data.items()
                                     if k in desired_ability_keys)

        abilities_to_return.append(ability_data_filtered)

    return abilities_to_return


def get_pokemon_moves(pokemon_data: dict) -> list[dict]:
    """Returns list of pokemon moves from API"""

    pokemon_moves_to_transform = []

    desired_move_keys = {"accuracy",
                         "flavor_text_entries", "names", "power",
                         "pp", "priority", "damage_class"}

    pokemon_moves = pokemon_data["moves"]

    for move in pokemon_moves:
        move_url = move["move"]["url"]
        move_data = api_request_data(move_url)
        move_data_filtered = dict((k, v) for k, v
                                  in move_data.items()
                                  if k in desired_move_keys)

        pokemon_moves_to_transform.append(move_data_filtered)

    return pokemon_moves_to_transform


def extract_single_pokemon(url: str) -> None:
    """Extracts data associated with one pokemon from URL provided"""

    data = api_request_data(url)

    pokemon_data_to_transform = {}

    pokemon_stats = get_pokemon_stats(data)
    pokemon_data_to_transform["stats"] = pokemon_stats

    pokemon_abilities = get_pokemon_abilities(data)
    pokemon_data_to_transform["abilities"] = pokemon_abilities

    pokemon_moves = get_pokemon_moves(data)
    pokemon_data_to_transform["moves"] = pokemon_moves

    pokemon_data_to_transform["name"] = data["name"]

    return pokemon_data_to_transform


def extract_all_pokemon_urls() -> list[str]:
    """Extracts all pokemon urls (for main.py)"""

    pokemon_count = get_pokemon_count()

    pokemon_urls = get_pokemon_urls(pokemon_count)

    return pokemon_urls


def extract_all_pokemon() -> None:
    """Extracts all pokemon from the API"""

    pokemon_count = get_pokemon_count()

    pokemon_urls = get_pokemon_urls(pokemon_count)

    for url in pokemon_urls:

        pokemon_data = extract_single_pokemon(url)

        break


if __name__ == "__main__":

    extract_all_pokemon()

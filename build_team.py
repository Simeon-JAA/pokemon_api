"""Handles all functions related to building a team selected pokemon"""

from time import sleep
import requests


def api_request_data(api_url: str) -> dict:
    """Returns the dictionary response from the API"""

    try:
        api_response = requests.get(api_url)

    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as Err:
        Err("Error: Unable to make a successful connection with API!")

    if api_response.status_code != 200:
        raise Exception("Error: Not a 200 status code!")

    data = api_response.json()

    return data


def get_all_pokemon_names() -> list:
    """Returns names of all pokemon on database """

    pokemon_data_limited = api_request_data(
        "https://pokeapi.co/api/v2/pokemon")

    total_pokemon = pokemon_data_limited["count"]

    pokemon_data_all = api_request_data(
        f"https://pokeapi.co/api/v2/pokemon?offset=0&limit={total_pokemon}")

    pokemon_data_all = pokemon_data_all["results"]

    pokemon_names = [pokemon["name"] for pokemon in pokemon_data_all]

    return pokemon_names


def get_pokemon_data(pokemon_name: str) -> dict:
    """Returns pokemon data from API"""

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    pokemon_data = api_request_data(url)

    return pokemon_data


def filter_pokemon_stats(pokemon_data: dict) -> dict:
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


class Pokemon():
    """Pokemon class"""

    def __init__(self, name: str, pokemon_data: dict) -> None:
        self._all_pokemon_data = get_pokemon_data(name)
        self._name = name.title()
        self._stats = filter_pokemon_stats(self._all_pokemon_data)

    @property
    def name(self) -> str:
        """Returns pokemon name"""
        return self._name

    @property
    def stats(self) -> dict:
        """Returns pokemon's stats"""
        return self._stats


class PokemonTeam():
    """Class for creating a team of pokemon"""

    def __init__(self, team_name: str) -> None:

        # TODO figure out how to move edge cases into setter
        if not isinstance(team_name, str):
            raise TypeError("Error: Team nam must be a string!")

        if len(team_name) < 4:
            raise ValueError(
                "Error: Team name must be longer than 4 characters!")

        if len(team_name) > 20:
            raise ValueError(
                "Error: Team name must be shorter than 20 characters!")

        if len(team_name) == team_name.count(" "):
            raise ValueError("Error: Team name cannot be empty spaces!")

        self._team_name = team_name
        self._current_team = []
        self._current_team_max_pokemon = 4
        self._reserve_team = []

    @property
    def team_name(self) -> str:
        """Returns team name"""
        return self._team_name

    # TODO move edge cases to setter
    @team_name.setter
    def team_name(self, value: str) -> None:

        self._team_name = value

    @property
    def current_team(self) -> list:
        """Returns list of the current team"""
        return self._current_team

    @property
    def reserve_team(self) -> list:
        """Returns list of the reserve team"""
        return self._reserve_team

    @property
    def current_team_max_pokemon(self) -> list:
        """Returns max pokemon allowed in current team"""
        return self._current_team_max_pokemon

    def add_pokemon_to_current_team(self, pokemon: Pokemon) -> None:
        """Adds pokemon to team"""

        if not isinstance(pokemon, Pokemon):
            raise TypeError(
                "Error: You cannot add a non-pokemon to your current team!")

        if len(self.current_team) == self.current_team_max_pokemon:
            raise Exception("Error: Your current team of pokemon is full!")

        self.current_team.append(pokemon)


if __name__ == "__main__":

    pokemon_names = get_all_pokemon_names()

    while True:

        user_pokemon_name = input("Please chose your pokemon: ").lower()

        if user_pokemon_name not in pokemon_names:
            print("Not found")

        else:
            print("Found")
            sleep(0.5)
            print("Adding to team!")
            pokemon_data = get_pokemon_data(user_pokemon_name)
            user_pokemon = Pokemon(user_pokemon_name, pokemon_data)
            print(user_pokemon.stats)

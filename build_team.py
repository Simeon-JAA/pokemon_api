"""Handles all functions related to building a team selected pokemon"""

import re
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


def get_all_pokemon_names() -> list[str]:
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


def pass_pokemon_team_name_conditions(team_name: str) -> bool:
    """If team name passes guard clause, then return the team name"""

    if not isinstance(team_name, str):
        raise TypeError("Error: Team name should be a string!")

    full_match = re.fullmatch(
        "[(^\w\d)\s(\w\d$)\-\_\(\)]{3,20}(([\s]{1})([\w\d]+)){1,3}?", team_name)

    if not full_match:
        raise ValueError("Error: Team name is invalid!")

    return True


class Pokemon():
    """Pokemon class"""

    def __init__(self, name: str) -> None:
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

        if not isinstance(team_name, str):
            raise TypeError("Error: Team nam must be a string!")

        if pass_pokemon_team_name_conditions(team_name):
            self._team_name = team_name

        self._current_team = []
        self._current_team_max_pokemon = 4
        self._reserve_team = []

    @property
    def team_name(self) -> str:
        """Returns team name"""
        return self._team_name

    @team_name.setter
    def team_name(self, value: str) -> None:
        """Team name setter"""

        if not isinstance(value, str):
            raise TypeError("Error: Team name should be a string!")

        if pass_pokemon_team_name_conditions(value):
            print(f"Team name has successfully been changed to {value}!")
            self._team_name = value

    @property
    def current_team(self) -> list[Pokemon]:
        """Returns list of the current team"""
        return self._current_team

    @property
    def reserve_team(self) -> list[Pokemon]:
        """Returns list of the reserve team"""
        return self._reserve_team

    @property
    def current_team_max_pokemon(self) -> int:
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


def build_initial_pokemon_team(pokemon_team: PokemonTeam, pokemon_names: list[str]) -> PokemonTeam:
    """Will build the initial pokemon team"""

    current_team = pokemon_team.current_team

    current_team_names = [x.name.lower() for x in current_team]

    max_team_members = pokemon_team.current_team_max_pokemon
    team_members = 0

    while team_members < max_team_members:

        name = input("Please chose your pokemon: ").lower()

        if name not in pokemon_names:
            print("Error: Pokemon not found!")

        elif name in current_team_names:
            print("Error: Pokemon already in team!")

        else:
            print("Pokemon found!")
            sleep(0.5)
            pokemon_to_add = Pokemon(name)
            print(f"Adding {name.title()} to team!")
            pokemon_team.add_pokemon_to_current_team(pokemon_to_add)
            team_members += 1

    return pokemon_team


if __name__ == "__main__":

    pokemon_names = get_all_pokemon_names()

    pokemon_team = PokemonTeam("Example Team")

    pokemon_team = build_initial_pokemon_team(pokemon_team, pokemon_names)

    for pokemon in pokemon_team.current_team:
        print(pokemon.name)

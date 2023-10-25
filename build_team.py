"""Handles all functions related to building a team selected pokemon"""

import re


class Pokemon():
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name


class Pokemon_Team():
    """Class for creating a team of pokemon"""

    def __init__(self, team_name: str,) -> None:

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

"""Handles all functions related to building a team selected pokemon"""

import re


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

    @property
    def team_name(self) -> str:
        """Returns team name"""
        return self._team_name

    @team_name.setter
    def team_name(self, value: str) -> None:

        self._team_name = value

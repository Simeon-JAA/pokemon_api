"""Testing file for build_team"""

import pytest

from build_team import PokemonTeam


def test_class_pokemon_team_invalid_name():
    """Tests exception raised for creating a team name with just a number"""

    with pytest.raises(Exception):
        PokemonTeam(10)


def test_class_pokemon_team_invalid_name_too_short():
    """Tests exception is raised if team name is under 4 characters"""

    with pytest.raises(Exception):
        PokemonTeam("te")


def test_class_pokemon_team_invalid_name_too_long():
    """Tests exception is raised if team name is over 20 characters"""

    with pytest.raises(Exception):
        PokemonTeam("This name is definitely too long for a team name!")


def test_class_pokemon_team_invalid_name_empty_spaces():
    """Tests exception is raised if team name is empty spaces"""

    with pytest.raises(Exception):
        PokemonTeam("      ")


def test_class_pokemon_team_invalid_name_left_blank():
    """Tests exception is raised if team name is left blank"""

    with pytest.raises(Exception):
        PokemonTeam("")

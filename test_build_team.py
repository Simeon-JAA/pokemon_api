"""Testing file for build_team"""

import pytest

from build_team import PokemonTeam
from build_team import pass_pokemon_team_name_conditions


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


def test_pass_pokemon_team_name_conditions_base_case_1():
    """Test base case for pass_pokemon_team_name_conditions"""

    team_name = "Example Team 1"

    assert pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_base_case_2():
    """Test base case for pass_pokemon_team_name_conditions"""

    team_name = "My Team 1"

    assert pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_base_case_3():
    """Test base case for pass_pokemon_team_name_conditions"""

    team_name = "Thunder Team"

    assert pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_test_exception_1():
    """Test exception raised for pass_pokemon_team_name_conditions with bad input"""

    team_name = 5
    with pytest.raises(Exception):
        pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_test_exception_2():
    """Test exception raised for pass_pokemon_team_name_conditions with bad input"""

    team_name = ""
    with pytest.raises(Exception):
        pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_test_exception_3():
    """Test exception raised for pass_pokemon_team_name_conditions with bad input"""

    team_name = "       "
    with pytest.raises(Exception):
        pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_test_exception_4():
    """Test exception raised for pass_pokemon_team_name_conditions with bad input"""

    team_name = "3     6    g   s  "
    with pytest.raises(Exception):
        pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_test_exception_5():
    """Test exception raised for pass_pokemon_team_name_conditions with bad input"""

    team_name = "___!_'/d44w _dd???"
    with pytest.raises(Exception):
        pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_test_exception_6():
    """Test exception raised for pass_pokemon_team_name_conditions with bad input"""

    team_name = "2"
    with pytest.raises(Exception):
        pass_pokemon_team_name_conditions(team_name)


def test_pass_pokemon_team_name_conditions_test_exception_7():
    """Test exception raised for pass_pokemon_team_name_conditions with bad input"""

    team_name = "THIS TEAM NAME IS DEFINITELY TOO LONG FOR WHAT I AM BUILDING"
    with pytest.raises(Exception):
        pass_pokemon_team_name_conditions(team_name)

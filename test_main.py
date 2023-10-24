"""Testing file for main"""

import pytest

from main import get_pokemon_moves, get_pokemon_stats, get_pokemon_dimensions


def test_get_pokemon_moves_invalid_input_raises_exception():
    """Tests exception should be raises if the input for get_pokemon_moves isn't a dict"""

    with pytest.raises(Exception):
        get_pokemon_moves("Not a pokemon")


def test_get_pokemon_moves_missing_field_raises_exception(fake_pokemon_bad_data):
    """Tests exception should be raises if the input for get_pokemon_moves isn't a dict"""

    with pytest.raises(Exception):
        get_pokemon_moves(fake_pokemon_bad_data)


def test_get_pokemon_stats_invalid_input_raises_exception():
    """Tests exception should be raises if the input for get_pokemon_stats isn't a dict"""

    with pytest.raises(Exception):
        get_pokemon_stats("Not a pokemon")


def test_get_pokemon_stats_missing_field_raises_exception(fake_pokemon_bad_data):
    """Tests exception should be raises if the input for get_pokemon_stats isn't a dict"""

    with pytest.raises(Exception):
        get_pokemon_stats(fake_pokemon_bad_data)


def test_get_pokemon_stats_contains_hp(fake_pokemon_pikachu):
    """Tests hp field is in the result of get_pokemon_stats"""

    result = get_pokemon_stats(fake_pokemon_pikachu)

    assert "hp" in result


def test_get_pokemon_stats_contains_stats(fake_pokemon_pikachu):
    """Tests correct stat fields are in the result of get_pokemon_stats"""

    result = get_pokemon_stats(fake_pokemon_pikachu)

    assert "hp" in result
    assert "attack" in result
    assert "defense" in result
    assert "special-attack" in result
    assert "special-defense" in result


def test_get_pokemon_stats_contains_stats(fake_pokemon_pikachu):
    """Tests correct stat fields are in the result of get_pokemon_stats"""

    result = get_pokemon_stats(fake_pokemon_pikachu)

    assert "hp" in result
    assert "attack" in result
    assert "defense" in result
    assert "special-attack" in result
    assert "special-defense" in result


def test_get_pokemon_negative_stats_raise_exception(fake_pokemon_pikachu_bad_stats):
    """Tests exception is raised if any stats from get_pokemon_stats are negative"""

    with pytest.raises(Exception):
        get_pokemon_stats(fake_pokemon_pikachu_bad_stats)


def test_get_pokemon_dimensions_wrong_input_raises_exception():
    """Tests exception is raised if wrong input is given to function get_pokemon_dimensions"""

    with pytest.raises(Exception):
        get_pokemon_dimensions("This is not a pokemon")


def test_get_pokemon_dimensions_no_fields_raises_exception(fake_pokemon_bad_data):
    """Tests exception is raised if fields are missing in function get_pokemon_dimensions"""

    with pytest.raises(Exception):
        get_pokemon_dimensions(fake_pokemon_bad_data)


def test_get_pokemon_dimensions_negative_values_raise_exception(fake_pokemon_pikachu_bad_stats):
    """Tests exception is raised if weight and height field values are negative
    in missing in function get_pokemon_dimensions"""

    with pytest.raises(Exception):
        get_pokemon_dimensions(fake_pokemon_pikachu_bad_stats)


def test_get_pokemon_dimensions_base_case_1(fake_pokemon_pikachu):
    """Tests function get_pokemon_dimensions returns the correct data"""

    result = get_pokemon_dimensions(fake_pokemon_pikachu)

    assert fake_pokemon_pikachu["height"] == result["height"]
    assert fake_pokemon_pikachu["weight"] == result["weight"]

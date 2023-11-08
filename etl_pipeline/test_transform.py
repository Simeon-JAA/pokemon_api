"""Testing file for transform"""

from transform import set_abilities_language, filter_flavor_text_entries
from transform import filter_effect_entries


def test_filter_flavor_text_entries_version_group_changed_to_string(mock_flavor_text_entries_three_en_two_fr):
    """Tests version group has been changed to string in filter_flavor_text_entries"""

    result = filter_flavor_text_entries(
        mock_flavor_text_entries_three_en_two_fr)

    for item in result:
        assert isinstance(item["version_group"], str)


def test_filter_flavor_text_entries_version_group_correct(mock_flavor_text_entries_three_en_two_fr):
    """Tests version group is the correct text in filter_flavor_text_entries"""

    result = filter_flavor_text_entries(
        mock_flavor_text_entries_three_en_two_fr)

    for item in result:
        assert 'mock pokemon version_group["name"]' in item["version_group"]


def test_filter_flavor_text_entries_english_list_length(mock_flavor_text_entries_three_en_two_fr):
    """Tests list is correct length after run through the function filter_flavor_text_entries (english)"""

    result = filter_flavor_text_entries(
        mock_flavor_text_entries_three_en_two_fr)

    assert len(result) == 3


def test_filter_flavor_text_entries_french_list_length(mock_flavor_text_entries_three_en_two_fr):
    """Tests list is correct length after run through the function filter_flavor_text_entries (french)"""

    result = filter_flavor_text_entries(
        mock_flavor_text_entries_three_en_two_fr, 'fr')

    assert len(result) == 2


def test_filter_effect_entries_check_list_length_english(mock_effect_entries_four_en_three_es):
    """Test for filter_effect_entries to check correct list length"""

    result = filter_effect_entries(mock_effect_entries_four_en_three_es)

    assert len(result) == 4


def test_filter_effect_entries_check_list_length_spanish(mock_effect_entries_four_en_three_es):
    """Test for filter_effect_entries to check correct list length (spanish)"""

    result = filter_effect_entries(mock_effect_entries_four_en_three_es, "es")

    assert len(result) == 3


def test_filter_effect_entries_check_list_correct_keys(mock_effect_entries_four_en_three_es):
    """Test filter_effect_entries returns a list of dictionaries with the correct keys"""

    result = filter_effect_entries(mock_effect_entries_four_en_three_es, "es")

    for entry in result:
        assert list(entry.keys()) == ["effect", "short_effect"]


def test_filter_effect_entries_check_effect_value_english(mock_effect_entries_four_en_three_es):
    """Tests correct effect value is returned in filter_effect_entries (english)"""

    result = filter_effect_entries(mock_effect_entries_four_en_three_es)

    for entry in result:
        assert "mock effect (english)" in entry["effect"]


def test_filter_effect_entries_check_effect_value_spanish(mock_effect_entries_four_en_three_es):
    """Tests correct effect value is returned in filter_effect_entries (spanish)"""

    result = filter_effect_entries(mock_effect_entries_four_en_three_es, "es")

    for entry in result:
        assert "mock effect (spanish)" in entry["effect"]


def test_filter_effect_entries_check_short_effect_value_english(mock_effect_entries_four_en_three_es):
    """Tests correct short_effect value is returned in filter_effect_entries (english)"""

    result = filter_effect_entries(mock_effect_entries_four_en_three_es)

    for entry in result:
        assert "mock short effect (english)" in entry["short_effect"]


def test_filter_effect_entries_check_short_effect_value_spanish(mock_effect_entries_four_en_three_es):
    """Tests correct short_effect value is returned in filter_effect_entries (spanish)"""

    result = filter_effect_entries(mock_effect_entries_four_en_three_es, "es")

    for entry in result:
        assert "mock short effect (not english)" in entry["short_effect"]

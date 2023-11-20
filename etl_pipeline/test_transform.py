"""Testing file for transform"""

from transform import set_abilities_language, filter_flavor_text_entries
from transform import filter_effect_entries, filter_ability_name


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


def test_filter_ability_name_returns_dict(mock_names_en_sp_fr_zh):
    """Tests function filter_ability_name returns dictionary"""

    result = filter_ability_name(mock_names_en_sp_fr_zh)

    assert isinstance(result, dict)


def test_filter_ability_name_returns_name_english(mock_names_en_sp_fr_zh):
    """Tests function filter_ability_name returns correct name"""

    result = filter_ability_name(mock_names_en_sp_fr_zh)

    assert "mock ability name (english)" in result["name"]


def test_filter_ability_name_returns_name_spanish(mock_names_en_sp_fr_zh):
    """Tests function filter_ability_name returns correct name (spanish)"""

    result = filter_ability_name(mock_names_en_sp_fr_zh, "es")

    assert "mock ability name (spanish)" in result["name"]


def test_filter_ability_name_returns_name_french(mock_names_en_sp_fr_zh):
    """Tests function filter_ability_name returns correct name (french)"""

    result = filter_ability_name(mock_names_en_sp_fr_zh, "fr")

    assert "mock ability name (french)" in result["name"]


def test_filter_ability_name_returns_name_chinese(mock_names_en_sp_fr_zh):
    """Tests function filter_ability_name returns correct name (chinese)"""

    result = filter_ability_name(mock_names_en_sp_fr_zh, "zh")

    assert "mock ability name (chinese)" in result["name"]


def test_set_abilities_language_base_case_1(mock_extracted_pokemon_data):
    """Tests abilities is returned containing only english entries"""

    result = set_abilities_language(mock_extracted_pokemon_data)

    pokemon_abilities_filtered = result["abilities"]

    for ability in pokemon_abilities_filtered:

        for effect_entry in ability["effect_entries"]:

            assert 'english' in effect_entry["effect"]

        for flavor_text_entry in ability["flavor_text_entries"]:

            assert 'english' in flavor_text_entry["flavor_text"]

        assert "english" in ability["names"]["name"]

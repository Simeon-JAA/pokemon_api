"""Testing file for transform"""

from transform import set_abilities_language, filter_flavor_text_entries


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

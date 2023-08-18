from scores import calculate_letter_score, calculate_word_score, get_random_letter, build_rack, create_bag, get_letter_from_bag


def test_calculate_value_of_a():
    assert calculate_letter_score({99: ['A']}, 'A') == 99


def test_calculate_value_of_j():
    assert calculate_letter_score('J') == 8


def test_word_score():
    assert calculate_word_score('RAMP') == 8


def test_calculate_value_of_empty():
    assert calculate_letter_score('') == 0


def test_calculate_empty_word():
    assert calculate_word_score('') == 0


def test_random_letter_returns_a_string():
    assert isinstance(get_random_letter(), str)


def test_building_rack_is_string():
    assert isinstance(build_rack(), list)


def test_rack_length_is_seven():
    assert len(build_rack()) == 7


def test_create_bag_is_list():
    assert isinstance(create_bag({4: ['A']}), list)
    assert create_bag({4: ['A']}) == ['A', 'A', 'A', 'A']


def test_get_letter_from_bag():
    assert isinstance(get_letter_from_bag(['E', 'A']), str)

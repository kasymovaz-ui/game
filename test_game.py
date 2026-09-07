from game import add_coins, check_result, validate_choice


def test_add_coins():
    assert add_coins(10, 5) == 15


def test_add_coins_zero():
    assert add_coins(20, 0) == 20


def test_player_wins():
    assert check_result(50) == "win"


def test_player_loses():
    assert check_result(49) == "lose"


def test_valid_choice():
    assert validate_choice("1") is True
    assert validate_choice("2") is True


def test_invalid_choice():
    assert validate_choice("3") is False
    assert validate_choice("abc") is False
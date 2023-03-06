from bank import value


def test_values():
    assert value("hello") == "$0"
    assert value("H") == "$20"
    assert value("Not Hello") == "$100"
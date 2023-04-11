from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("512.512.512.512") is False
    assert validate("1.2.3.1000") is False
    assert validate("cat") is False

from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("cat") == "dog"
    assert convert("3/4/3") == "cat"
    assert convert("9/1") == 9


def test_gauge():
    assert gauge(99.5) == "F"
    assert gauge(0.5) == "E"
    assert gauge(75) == "75%"

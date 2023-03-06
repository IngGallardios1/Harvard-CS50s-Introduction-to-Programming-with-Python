from twttr import shorten


def test_strings():
    assert shorten("HOLA") == "HL"
    assert shorten("mundo") == "mnd"
    assert shorten("Parangaricutirimicuaro") == "Prngrctrmcr"


def test_numbers():
    assert shorten("1") == "1"
    assert shorten("-1") == "-1"
    assert shorten("0") == "0"

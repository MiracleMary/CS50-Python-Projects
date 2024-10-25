import pytest
from twttr import shorten

def test_no_vowels():
    assert shorten("fly") == "fly"

def test_with_vowels():
    assert shorten("world") == "wrld"

def test_all_vowels():
    assert shorten("aeiou") == ""

def test_empty_string():
    assert shorten("") == ""

def test_upper_case():
    assert shorten("HELLO") == "HLL"

def test_with_numbers():
    assert shorten("hello789") == "hll789"

def test_with_special_characters():
    assert shorten("Hello!!!...") == "Hll!!!..."


if "__name__" == "__main__":
    pytest.main(["-s"])

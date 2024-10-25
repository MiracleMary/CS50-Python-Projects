import pytest
from plates import is_valid


def test_valid_plate():
    assert is_valid("ABCD12") == True

def test_invalid_plate():
    assert is_valid("ABCD123") == False

def test_valid_plate_cs():
    assert is_valid("CS50") == True

def test_invalid_plate_number():
    assert is_valid("CS05") == False

def test_invalid_plate_character():
    assert is_valid("AB.12!") == False

def test_invalid_plate_alpha():
    assert is_valid("123ABC") == False


if __name__ == "__main__":
    pytest.main()

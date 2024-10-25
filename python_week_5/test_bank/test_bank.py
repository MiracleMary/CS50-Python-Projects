import pytest
from bank import value


def test_hello():
    assert value("hello world") == 0

def test_hi():
    assert value("hi there") == 20

def test_g():
    assert value("goodbye") == 100

def test_case():
    assert value("HELLO everyone") == 0

def test_h_case():
    assert value("How are you?") == 20

def test_low_case():
    assert value("what's up?") == 100


if __name__ == "__main__":
    pytest.main()

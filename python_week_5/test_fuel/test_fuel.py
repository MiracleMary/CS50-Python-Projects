import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("5/10") == 50

def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_F():
    assert gauge(99) == "F"

def test_gauge_half():
    assert gauge(50) == "50%"

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_convert_invalid_value():
    with pytest.raises(ValueError):
        convert("10/5")

if __name__ == "__main__":
    pytest.main()

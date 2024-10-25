import pytest
from working import convert

def test_valid_12_hour_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_12_hour_format_with_minutes():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9:45 AM to 5:45 PM") == "09:45 to 17:45"

def test_valid_12_hour_format_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_invalid_12_hour_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

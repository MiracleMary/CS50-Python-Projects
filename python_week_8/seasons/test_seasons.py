from datetime import date
import pytest
from seasons import calculate_age_in_minutes, format_minutes_in_words

def test_calculate_age_in_minutes():
    birthdate = date(2000, 1, 1)
    age_in_minutes = calculate_age_in_minutes(birthdate)
    assert age_in_minutes == 12890880

    birthdate = date(1990, 5, 13)
    age_in_minutes = calculate_age_in_minutes(birthdate)
    assert age_in_minutes == 17959680


def test_format_minutes_in_words():
    assert format_minutes_in_words(525600) == "Five hundred twenty-five thousand, six hundred"

    assert format_minutes_in_words(0) == "Zero"


if __name__ == "__main__":
    pytest.main()

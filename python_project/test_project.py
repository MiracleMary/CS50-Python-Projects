import pytest
from project import convert_scores_to_grades, grade_weight, grade_class

def test_convert_scores_to_grades():
    assert convert_scores_to_grades(65) == "B"
    assert convert_scores_to_grades(20) == "F"

def test_grade_weight():
    assert grade_weight("A", 3) == 15
    assert grade_weight("D", 2) == 4

def test_grade_class():
    assert grade_class(4.46) == "YOU'RE IN SECOND CLASS UPPER! WORK HARDER!"
    assert grade_class(4.50) == "YOU'RE IN FIRST CLASS! KEEP IT UP!"

if __name__ == "__main__":
    pytest.main()

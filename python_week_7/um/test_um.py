from um import count

def test_single_um():
    assert count("hello, um, world") == 1

def test_no_um():
    assert count("hello") == 0

def test_multiple_um():
    assert count("Um, thanks, um...") == 2

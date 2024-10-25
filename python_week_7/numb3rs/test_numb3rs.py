from numb3rs import validate

def test_valid_ipv4():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_invalid_ipv4():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False


def test_string_ipv4():
    assert validate("cat") == False
    assert validate("bat") == False

def test_letter_ipv4():
    assert validate("192.168.a.0") == False
    assert validate("a.231.b.231") == False

def test_dots_ipv4():
    assert validate("168.168..168.168") == False
    assert validate("255.1.1.0.") == False

def test_empty_ipv4():
    assert validate("") == False

def test_negative_ipv4():
    assert validate("123.-123.0.-1") == False




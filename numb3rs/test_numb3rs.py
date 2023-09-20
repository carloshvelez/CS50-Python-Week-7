from numb3rs import validate

def test_ip_valid():
    assert validate("255.254.253.250") == True
    assert validate("0.0.0.0") == True
    assert validate("5.4.3.2") == True

def test_ip_invalid():
    assert validate("256.254.253.250") == False
    assert validate("0.0.0") == False
    assert validate("5.4.3.2.1") == False
    assert validate("255") == False
    assert validate("245.256.257.258") == False



from numb3rs import validate

def test_validate():
    assert validate("0.1.2.3") == False
    assert validate("256.3.4.5") == False
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4") == True

from bank import value

def test_value():
        assert value("hello, newman") == 0
        assert value("hi, newman") == 20
        assert value("yo, newman") == 100
        assert value("abcdef") == 100
        assert value("0000") == 100
        assert value("???") == 100
        assert value("HELLO") == 0
        assert value("   ") == 100
        assert value("   ee hello") == 100
        assert value("   hello") == 0
        assert value("False") == 100

import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("4/4") == 100
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("1/3") == 33
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(67) == "67%"
    assert gauge(33) == "33%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

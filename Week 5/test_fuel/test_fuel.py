import pytest
from fuel import convert, gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_conversion():
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    assert convert("1/4") == 25
    assert convert("0/5") == 0

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")


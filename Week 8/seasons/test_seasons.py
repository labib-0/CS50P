import pytest
from seasons import convert_inflect

def test_convert_inflect():
    assert convert_inflect(10) == "Ten minutes"
    assert convert_inflect(100) == "One hundred minutes"

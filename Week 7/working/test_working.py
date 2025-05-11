import pytest
from working import convert


def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:10 PM") == "09:00 to 17:10"
    assert convert("10 PM to 8:56 AM") == "22:00 to 08:56"
    assert convert("11:34 PM to 9:50 AM") == "23:34 to 09:50"


def test_valueerror():
    with pytest.raises(ValueError):
        convert("9 am to 5 pm")
    with pytest.raises(ValueError):
        convert("9AM")
    with pytest.raises(ValueError):
        convert("9:78 AM to 5:99 PM")
    with pytest.raises(ValueError):
        convert("9:43 am to 5:00 pm")

import pytest
from working import convert

def test_incorrect_numbers():
    with pytest.raises(ValueError):
        convert("14 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("12:00 AM to 07:60 PM")

def test_incorrec_format():
    with pytest.raises(ValueError):
        convert("14 AM 5 PM")

    with pytest.raises(ValueError):
        convert("12:00AM to07:00 PM")

def test_correct_format():
    assert convert("12:00 AM to 07:00 PM") == "00:00 to 19:00"

    assert convert("12 AM to 07 PM") == "00:00 to 19:00"



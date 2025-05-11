from plates import is_valid

def test_number_place():
    assert is_valid("ArT123") == True
    assert is_valid("ABu2CD") == False
    assert is_valid("avb12D") == False

def test_leading_zero():
    assert is_valid("yB019") == False
    assert is_valid("AC012") == False

def test_special_characters():
    assert is_valid("AB!123") == False
    assert is_valid("AB 123") == False
    assert is_valid("AB@12") == False

def test_valid_cases():
    assert is_valid("CS50") == True
    assert is_valid("CSAI") == True
    assert is_valid("HELLO") == True

def test_leading_num():
    assert is_valid("098765") == False
    assert is_valid("0987AD") == False
    assert is_valid("76") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("") == False
    assert is_valid("ABCDEFG") == False

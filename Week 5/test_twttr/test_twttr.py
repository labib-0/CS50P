from twttr import shorten
def test_OnlyVowel():
    assert shorten("AEIOU") == ""
    assert shorten("A e I o U") == "    "
    assert shorten("aeiou") == ""
def test_OnlyConsonent():
    assert shorten("BCD bcd bCd") == "BCD bcd bCd"
def test_mixed():
    assert shorten("I love Bangladesh") == " lv Bngldsh"
    assert shorten("Once , 8989+989=7889 ") == "nc , 8989+989=7889 "

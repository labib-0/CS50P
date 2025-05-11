from bank import value

def test_h():
    assert value('h') == 20
    assert value('H') == 20
    assert value('h what') == 20
def test_hello():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('heLLo, whats up') == 0
def test_empty():
    assert value('') == 100
def test_other():
    assert value('Good Morning') == 100
    assert value('Whats Up') == 100


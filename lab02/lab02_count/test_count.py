from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}

def test_double():
    assert count_char("aa") == {"a": 2}

def test_symbol():
    assert count_char("a!?!") == {"a": 1, "!": 2, "?": 1}

def test_number():
    assert count_char("2021") == {"2": 2, "0": 1, "1": 1}
    
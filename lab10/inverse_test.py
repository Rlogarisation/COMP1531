from inverse import inverse
from hypothesis import given, strategies

def test_specifications():
    assert inverse({1: 'A', 2: 'B', 3: 'A'}) == {'A': [1, 3], 'B': [2]}

def test_empty():
    assert inverse({}) == {}

def test_single_string():
    assert inverse({'key': 'value'}) == {'value': ['key']}

def test_multiple_strings():
    assert inverse({'key1': 'value1', 'key2': 'value2', 'key3': 'value1'}) == {'value1': ['key1', 'key3'], 'value2': ['key2']}
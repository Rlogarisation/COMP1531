from prefix import prefix_search
import pytest

def test_documentation():
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a") == { "ac": 1, "ab": 3}

def test_exact_match():
    assert prefix_search({"category": "math", "cat": "animal"}, "cat") == {"category": "math", "cat": "animal"}

def test_no_match():
    assert prefix_search({"category": "math", "cat": "animal"}, "roger") == {}

def test_no_dictionary():
    assert prefix_search({}, "") == {}
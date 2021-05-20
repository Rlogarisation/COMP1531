from divisors import divisors
from hypothesis import given, strategies
import pytest

def test_12():
    assert divisors(12) == {1,2,3,4,6,12}

def test_0():
    with pytest.raises(ValueError):
        assert divisors(0)

def test_negative():
    with pytest.raises(ValueError):
        assert divisors(-10)
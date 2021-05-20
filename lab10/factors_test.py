from factors import factors, is_prime
from hypothesis import given, strategies
import inspect
from pytest import raises

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(factors), "factors does not appear to be a generator"

def test_negative():
    with raises(ValueError):
        list(factors(-1))

def test_simple():
    assert list(factors(12)) == [2, 2, 3]
    assert list(factors(128)) == [2, 2, 2, 2, 2, 2, 2]

def test_prime():
    assert list(factors(13)) == [13]

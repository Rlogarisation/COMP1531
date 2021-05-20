'''
Tests for check_password()
'''
from password import check_password

def test_strong():
    assert check_password("UNSWIsTheBest2021") == "Strong password"
def test_moderate():
    assert check_password("goodweather1") == "Moderate password"
def test_poor():
    assert check_password("qwer") == "Poor password"
    assert check_password("iksn") == "Poor password"
    assert check_password("abc") == "Poor password"
def test_horrible():
    assert check_password("iloveyou") == "Horrible password"
    assert check_password("123456") == "Horrible password"
    assert check_password("password") == "Horrible password"
def test_symbol():
    assert check_password("!@#$") == "Poor password"
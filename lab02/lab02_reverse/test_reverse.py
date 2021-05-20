'''
Tests for reverse_words()
'''
from reverse import reverse_words

def test_example():
    assert reverse_words(["Hello World", "I am here"]) == ['World Hello', 'here am I']  
def test_three_letter():
    assert reverse_words(["I am Roger"]) == ['Roger am I']
def test_three_letter_multiple():
    assert reverse_words(["Good Day m8", "How are you", "fine thank you"]) == ['m8 Day Good', 'you are How', 'you thank fine']
def test_contain_number():
    assert reverse_words(["Hello", "I am 21 years old"]) == ['Hello', 'old years 21 am I']
def test_contain_symbol():
    assert reverse_words(["Test for special symbol", "OMG!!! FOR REAL???"]) == ['symbol special for Test', 'REAL??? FOR OMG!!!']

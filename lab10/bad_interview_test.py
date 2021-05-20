from bad_interview import bad_interview
import inspect

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(bad_interview), "bad_interview does not appear to be a generator"

def test_bad_interview():
    '''
    Check the first 20 numbers yielded by the iterator.
    '''
    g = bad_interview()
    first20 = [next(g) for _ in range(20)] # So it can follow up from where it freeze in yield
    assert first20 == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']


"""
You can use underscore(_) as a variable in looping:

## lopping ten times using _
for _ in range(5):
    print(_)

## iterating over a list using _
## you can use _ same as a variable
languages = ["Python", "JS", "PHP", "Java"]
for _ in languages:
    print(_)


"""


"""
The next() function returns the next item in an iterator.

You can add a default return value, to return if the iterable has reached to its end.

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)


apple
banana
cherry
"""
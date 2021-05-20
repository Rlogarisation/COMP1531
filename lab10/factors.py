'''
NOTE: This exercise assumes you have completed divisors.py
'''

from divisors import divisors

# You may find this helpful
def is_prime(n):
    return n != 1 and divisors(n) == {1, n}

def factors(n):
    '''
    A generator that generates the prime factors of n. For example
    >>> list(factors(12))
    [2,2,3]

    Params:
      n (int): The operand

    Yields:
      (int): All the prime factors of n in ascending order.

    Raises:
      ValueError: When n is <= 1.
    '''
    if n <= 1:
        raise ValueError("n must be a positive integer greater than 1")

    i = 2
    while i <= n:
        if is_prime(i) is True and n % i == 0:
            n /= i
            yield i
        else: 
            i += 1

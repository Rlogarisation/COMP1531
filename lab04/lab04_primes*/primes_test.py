import primes


def test_repeated_prime_number():
    assert(primes.factors(16) == [2, 2, 2, 2])
    
def test_non_repeated_prime_number():
    assert(primes.factors(21) == [3, 7])

def test_single_prime_number():
    assert(primes.factors(2) == [2])

def test_prime_number_zero():
    assert(primes.factors(0) == [])
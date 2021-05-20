import math

def factors(num):
    '''
    Returns a list containing the prime factors of 'num'. The primes should be
    listed in ascending order.

    For example:
    >>> factors(16)
    [2, 2, 2, 2]
    >>> factors(21)
    [3, 7]
    '''

    """
    i = 2
    listNum = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            listNum.append(i)
    if (num > 1):
        listNum.append(num)

    return listNum
    """
    # Standard answer:
    primes = []

    for i in range(2,int(math.sqrt(num))+1): 
        while num % i == 0:
            primes.append(i)
            num = int(num / i)

    if num > 2:
        primes.append(num)

    return primes

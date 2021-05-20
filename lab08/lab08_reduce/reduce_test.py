from reduce import reduce

def test_addition():
    assert(reduce(lambda x, y: x + y, [1,2,3,4,5,6,7]) == 28)

def test_multi():
    assert(reduce(lambda x, y: x * y, [1,2,3,4,5,6,7]) == 5040)

def test_double():
    assert(reduce(lambda x, y: x + y, [1.1,2.2,3.3,4.4,5.5,6.6,7.7]) == 30.8)

def test_negative():
    assert(reduce(lambda x, y: x + y, [1,-2,3,4,-5,-6,-7]) == -12)


from list_exercises import *

def test_reverse():
    l = ["how", "are", "you"]
    reverse_list(l)
    assert l == ["you", "are", "how"]

    j = ["good", "day", "m8"]
    reverse_list(j)
    assert j == ["m8", "day", "good"]

    k = ["nice", "to", "meet", "you"]
    reverse_list(k)
    assert k == ["you", "meet", "to", "nice"]

def test_min_positive():
    assert minimum([1, 2, 3, 10]) == 1
    assert minimum([20, 3, 57, 8888]) == 3
    assert minimum([1.3, 1.1, 3, 25]) == 1.1


def test_sum_positive():
    assert sum_list([7, 7, 7]) == 21
    assert sum_list([3, 7, 21]) == 31
    assert sum_list([27, 0, 1]) == 28
    assert sum_list([1.1, 7, 1.3]) == 9.4
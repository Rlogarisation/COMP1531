
"""
Standard answer:
from operator import mul
from functools import reduce

def product(iterable):
    return reduce(mul, iterable, 1)

def drykiss(inputs):
    return (min(inputs), product(inputs[:4]), product(inputs[1:]))

"""


def drykiss(my_list):
    # Find the minimum number out of list
    '''
    my_min = 999999
    for i in range(0, 5):
        if my_list[i] < my_min:
            my_min = my_list[i]
    '''
    my_min = min(my_list)

    # Multiply first 4 numbers from the list
    '''
    product = 1
    for i in range(0, 4):
        product = product * my_list[i]
    result = product
    '''


    # Multiply last 4 numbers from the list
    '''
    product = 1
    for i in range(1, 5):
        product = product * my_list[i]
    '''
    product = 1
    for i in range(0, 5):
        product = product * my_list[i]
    result = product / my_list[4]
    product = product / my_list[0]

    result = (my_min, result, product)
    return result
    
    

if __name__ == '__main__':
    a = input("Enter a: ")
    a = int(a)
    b = input("Enter b: ")
    b = int(b)
    c = input("Enter c: ")
    c = int(c)
    d = input("Enter d: ")
    d = int(d)
    e = input("Enter e: ")
    e = int(e)
    my_list = [a, b, c, d, e]
    result = drykiss(my_list)
    print("Minimum: " + str(result[0]))
    print("Product of first 4 numbers: ")
    print(f"  {result[1]}")
    print("Product of last 4 numbers")
    print(f"  {result[2]}")

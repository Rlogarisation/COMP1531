def reduce(f, xs):
    value = 0
    for i in range(0, len(xs)):
        if value == 0 and i == 0:
            value = f(xs[0], xs[1])
        elif i == 1:
            pass
        else:
            value = f(value, xs[i])
    return value


'''
if __name__ == '__main__':
    print(reduce(lambda x, y: x + y, [1,2,3,4,5]))
    print(reduce(lambda x, y: x * y, [1,2,3,4,5]))
'''
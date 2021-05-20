
def neighbours(iterable):
    '''
    A generator, that, given an iterable, yields the "neighbourhood" of each
    element. The neighbourhood is a tuple containing the element itself as well
    as the one that comes before and the one that comes after. For example,
    >>> list(neighbours([1,2,3,4]))
    [(1,2), (1,2,3), (2,3,4), (3,4)]

    Note that the first and last elements are pairs, while the rest are triples.

    Params:
      iterable (iterable): The iterable being processed. In the event it's empty,
      this generator should not yield anything. In the event it only contains
      one element, only that element should be yielded in a one-tuple.

    Yields:
      (tuple) : The neighbourhood of the current element.
    '''
    # Hint: Don't forget that iterables can produce values infinitely. You can't
    # rely on being able to retrieve all the elements at once.
    size = sum(1 for item in iterable)

    iterator = iter(iterable)

    if size == 0:
        return
    if size == 1:
        yield tuple(iterator)
        return

    for i in range(size):
        try:
            if i == 0:
                first, second, third = next(iterator), next(iterator), None
                yield (first, second)

            elif i == size - 1:
                if third is None:
                    yield (first, second)
                else:
                    yield (second, third)

            else:
                if third is None:
                    third = next(iterator)
                else:
                    first, second, third = second, third, next(iterator)
                yield (first, second, third)

        except StopIteration:
            yield
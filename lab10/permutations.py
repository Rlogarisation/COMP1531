def permutations(string):
    '''
    For the given string, compute the set of all permutations of the characters of that string. For example:
    >>> permutations('ABC')
    {'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'}

    Params:
      string (str): The string to permute

    Returns:
      (set of str): Each string in this set should be a permutation of the input string.
    '''
    perms_set = set()
    permutate(perms_set, string, 0)
    return perms_set

def permutate(perms_set, string, step):
    if step == len(string):
        perms_set.add(''.join(string))

    for i in range(step, len(string)):
        copy = list(string)

        copy[step], copy[i] = copy[i], copy[step]

        permutate(perms_set, copy, step + 1)
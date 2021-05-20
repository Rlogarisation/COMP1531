def roman(numerals):
    '''
    Given Roman numerals as a string, return their value as an integer. You may
    assume the Roman numerals are in the "standard" form, i.e. any digits
    involving 4 and 9 will always appear in the subtractive form.

    For example:
    >>> roman("II")
    2
    >>> roman("IV")
    4
    >>> roman("IX")
    9
    >>> roman("XIX")
    19
    >>> roman("XX")
    20
    >>> roman("MDCCLXXVI")
    1776
    >>> roman("MMXIX")
    2019
    '''
    """
    # Use a loop to iterate through the Roman numeral to figure out their value.
    roman_normal = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    roman_special = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    counter = 0
    result = 0
    while (counter < len(numerals)):
        if numerals[counter : counter + 2] in roman_special and counter + 1 < len(numerals):
            result += roman_special[numerals[counter : counter + 2]]
            counter += 2
        else:
            result += roman_normal[numerals[counter]]
            counter += 1
    return result
    """

    # Standard answer:
    roman = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
    ]
    value = 0
    i = 0
    while i < len(numerals):
        for x, v in roman: # pragma: no cover
            if i+len(x) <= len(numerals) and x == numerals[i:i+len(x)]:
                value += v

                i += len(x)
                break

    return value



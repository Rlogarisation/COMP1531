from roman import roman

def test_no_special_character():
    assert(roman("V") == 5)
    assert(roman("VI") == 6)
    assert(roman("VII") == 7)

def test_special_character():
    assert(roman("IV") == 4)
    assert(roman("IX") == 9)


def test_combine_character():
    assert(roman("XIX") == 19)
    assert(roman("MDCCLXXVI") == 1776)
    assert(roman("MMXIX") == 2019)
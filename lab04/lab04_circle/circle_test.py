from circle import Circle

def test_small():
    c = Circle(3)
    assert(round(c.circumference(), 1) == 18.8)
    assert(round(c.area(), 1) == 28.3)


def test_larger_radius():
    c = Circle(100)
    assert(round(c.circumference(), 1) == 628.3)
    assert(round(c.area(), 1) == 31415.9)

def test_double_radius():
    c = Circle(10.5)
    assert(round(c.circumference(), 1) == 66.0)
    assert(round(c.area(), 1) == 346.4)

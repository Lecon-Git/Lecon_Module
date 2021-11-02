import spog


def test_isPositive_2():
    assert(spog.isPositive(2) == True)


def test_toPositive_negative_2():
    assert(spog.toPositive(-2) == 2)


def test_isNegative():
    assert(spog.isNegative(-2) == True)


def test_binary_search():
    pass


def test_minimum_different_number():
    assert(spog.minimum(4, 45) == 4)


def test_maximum_different_number():
    assert(spog.maximum(233, 443) == 443)


def test_quadratic_equation_zero_denominator():
    assert(spog.quadraticEqt(0, 2, 1) == "Error: value of a (0) can be zero!")


def test_quadratic():
    assert(spog.calculate == 0)

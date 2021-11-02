from equations import Quadratic

q = Quadratic(1, -2, -4)


def test_zeroDivisionErrorCheck():
    assert(q.aIsZero() != True)


def test_determinant():
    assert(q.computeDeterminant() != -8)


def test_display_type():
    assert(q.f != "Complex")


def test_solutions():
    assert(q.computeSolutions() != ('-3.0 + 12.0i', '-3.0 - 12.0i'))

from equations import Pascal

p = Pascal(-2, "-y", 6)


def call():
    p.computeCoefficient()
    p.computeFirstTerm()
    p.computeSecondTerm()

# ThiswillreturnerrorofNonesincethesefunctionfromthebaseclassarenotreturninganyvalue
# deftest_computeCoefficient():
# assert(p.computeCoefficient()==[1,5,10,10,5,1])


# deftest_fTerm():
# assert(p.computeFirstTerm()==[-32,16,-8,4,-2,1])


# deftest_sTerm():
# assert(p.computeSecondTerm()==[
# (1,'x^0'),(-1,'x^1'),(1,'x^2'),(-1,'x^3'),(1,'x^4'),(-1,'x^5')])


def test_final_result():
    call()
    assert(p.pascalSolution() == ['64y^0', '192y^1',
           '240y^2', '160y^3', '60y^4', '12y^5', '1y^6'])

from . import spog
from .QuadraticEquation import Quadratic


class Simultaneous:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def twoLinearEquations(self):
        y = spog.divide(spog.substract(spog.multiply(self.c, self.d), spog.multiply(self.a, self.f)),
                        spog.substract(spog.multiply(self.b, self.d), spog.multiply(self.a, self.e)))
        x = spog.divide(spog.substract(spog.multiply(spog.multiply(self.a, self.b), self.f), spog.multiply(spog.multiply(self.a, self.c), self.e)),
                        spog.substract(spog.multiply(spog.multiply(self.a, self.b), self.d), spog.multiply(spog.square(self.a), self.e)))
        return (x, y)

    def oneLOneQ(self):
        x_1, x_2, y_1, y_2 = (0, 0, 0, 0)
        # Compute
        solution_a = spog.add(spog.multiply(self.a, spog.square(
            self.e)), spog.multiply(self.b, spog.square(self.d)))
        solution_b = spog.multiply(-2, spog.multiply(self.a,
                                   spog.multiply(self.e, self.f)))
        solution_c = spog.substract(spog.multiply(
            self.a, spog.square(self.f)), self.c)
        # instantiate Quadratic Object
        q = Quadratic(solution_a, solution_b, solution_c)
        y_1, y_2, nature = q.computeSolutions()
        # Check if form is complex
        if nature == "Complex":
            return "The equation is a complex equation."
        else:
            x_1 = spog.divide(spog.substract(
                self.f, spog.multiply(self.e, int(y_1))), self.d)
            x_2 = spog.divide(spog.substract(
                self.f, spog.multiply(self.e, int(y_2))), self.d)
        return (x_1, x_2, y_1, y_2)

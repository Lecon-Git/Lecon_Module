###
#   Implement simple and complex math's functions
#   Author and developer: Sunday P. Afolabi
#   Started on: 15-July-2021
#   By around: 9:00am
#   Initial Location: University of Jos, ICT
#   Privacy and Piracy Policy is applied
###

###
# import libraries
###
from . import spog


class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.f = ""
        self.d = 0

    def aIsZero(self):
        if self.a == 0:
            return True
        else:
            return False

    def computeDeterminant(self):
        self.d = spog.substract(spog.square(self.b), 4*self.a*self.c)
        if self.d == 0:
            self.f = "Identical"
        elif self.d > 0:
            self.f = "Distinct"
        else:
            self.f = "Complex"

    def computeSolutions(self):
        if self.aIsZero():
            return "Undefined equation because 'a' value is zero."
        else:
            self.computeDeterminant()
            if self.d == 0:
                # Compute identical form
                solution1 = str(spog.divide((-1)*self.b, 2*self.a))
                solution2 = str(solution1)
            elif self.d > 0:
                # Compute distinct form
                solution1 = str(spog.divide(
                    spog.add((-1)*self.b, spog.sqrt(self.d)), 2*self.a))
                solution2 = str(spog.divide(
                    spog.substract((-1)*self.b, spog.sqrt(self.d)), 2*self.a))
            else:
                # Compute complex form
                # Reverse determinant equation to get positive number and append i which implies sqrt(-1)
                self.d = spog.substract(4*self.a*self.c, spog.square(self.b))
                solution_dictionary = {
                    "solu1": {
                        "real_value": 0,
                        "imaginary_value": 0
                    },
                    "solu2": {
                        "real_value": 0,
                        "imaginary_value": 0
                    }
                }
            # These are integer values
            # Solution1
                solution_dictionary["solu1"]["real_value"] = spog.divide((
                    -1)*self.b, 2*self.a)
                solution_dictionary["solu1"]["imaginary_value"] = spog.divide(
                    self.d, 2*self.a)
            # Solution2
                solution_dictionary["solu2"]["real_value"] = spog.divide((
                    -1)*self.b, 2*self.a)
                solution_dictionary["solu2"]["imaginary_value"] = spog.divide(
                    self.d, 2*self.a)
            # Here we up case to string value to reflect complex indicator i.e sqrt(-1) => i
            # Join this piece of solutions together
                solution1 = str(solution_dictionary["solu1"]["real_value"]) + " + " + str(
                    solution_dictionary["solu1"]["imaginary_value"]) + "i"
                solution2 = str(solution_dictionary["solu2"]["real_value"]) + " - " + str(
                    solution_dictionary["solu2"]["imaginary_value"]) + "i"
        # return final result
            return (solution1, solution2, self.f)

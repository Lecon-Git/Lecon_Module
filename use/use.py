from quadratic import Quadratic
from simultaneous import Simultaneous
import sys

q = Quadratic(1, 3, 2)

solutions = q.computeSolutions()
try:
    x1, x2, nature = solutions
    print("------------------", end="")
    print("------------------\nSolutions are: {} and {}.\nThe nature of the equation is {}.\n------------------".format(
        x1, x2, nature), end="")
    print("------------------")
except ValueError as ve:
    print("Error: {}".format(solutions))
    sys.exit(1)
#print("Continuous if not error...")

s = Simultaneous(2, 1, -5, 4, 8, 9)
x, y = s.twoLinearEquations()
print("x = {} and y = {}.".format(x, y))
print("------------------", end="")
print("------------------")
try:
    x1, x2, y1, y2 = s.oneLOneQ()
    print("x1 = {}, x2 = {}, y1 = {} and y2 = {}.".format(x1, x2, y1, y2))
except ValueError as ve:
    print("Error: {}".format(s.oneLOneQ()))
    print("------------------", end="")
    print("------------------")
    sys.exit(1)

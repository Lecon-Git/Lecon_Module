from lecon import Quadratic

prompt = "Enter the coefficients of the equation ax^2 + bx + c = 0: "
a = int(input(prompt + "\na = "))
b = int(input("\nb = "))
c = int(input("\nc = "))

# q_equation = Quadratic(-1, 2, 3)
q_equation = Quadratic(a, b, c)

x1, x2, e_type = q_equation.computeSolutions()


def printResult():
        print("\n===================================================\n=")
        print("=\tSolution 1 is {0}, \n=\tSolution 2 is {1}, and \n=\tThe solution's type is {2}.\n=".format(x1, x2, e_type))
        print("===================================================")
        print("============= Powered by: SPa ICT Hub =============")
        print("===================================================\n")

printResult()
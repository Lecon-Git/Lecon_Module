from lecon import Simultaneous

prompt = "Enter the coefficients of the equation: \nax + by = c\ndx + ey = f "
a = int(input(prompt + "\na = "))
b = int(input("\nb = "))
c = int(input("\nc = "))
d = int(input("\nd = "))
e = int(input("\ne = "))
f = int(input("\nf = "))

simultaneous = Simultaneous(a, b, c, d, e, f)
# simultaneous = Simultaneous(10, -2, 40, 4, 2, 2)

def printResult():
        x, y = simultaneous.twoLinearEquations()
        print("\n===================================================\n=")
        print("=\tx is {0:.2f}, \n=\ty is {1:.2f}\n=".format(x, y))
        print("===================================================")
        print("============= Powered by: SPa ICT Hub =============")
        print("===================================================\n")

printResult()

# def printResult():
#         x1, x2, y1, y2 = simultaneous.oneLOneQ()
#         print("\n===================================================\n=")
#         print("=\tx1 = {0},\n=\tx2 = {1},\n=\ty1 = {2},\n=\ty2 = {3}\n=".format(x1, x2, y1, y2))
#         print("===================================================")
#         print("============= Powered by: SPa ICT Hub =============")
#         print("===================================================\n")
# printResult()
        

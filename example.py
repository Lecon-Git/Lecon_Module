from lecon import Pascal

prompt = "Pascal Triangle for nth power (firstTerm - secondTerm)^n e.g. (1 - x)^n"
try:
    fTerm = input(f"{prompt}\nEnter the first term: ")
    if "." in fTerm:
        fTerm = float(fTerm)
    else:
        fTerm = int(fTerm)
    sTerm = input("Enter the second term: ")
    power = int(input("Enter nth power: "))

    pascal = Pascal(firstTerm=fTerm, secondTerm=sTerm, index=power)
    output = pascal.pascalSolution()

    def printResult():
        print("\n===================================================\n=")
        print(f"= Pascal Triangle for {power}th power ({fTerm} + ({sTerm}))^{power}:\n=")
        pascal.formatResult(output)
        print("\n===================================================")
        print("============= Powered by: SPa ICT Hub =============")
        print("===================================================")
        print("\n")
        # pascal.print_tree()
except Exception as e:
    raise RuntimeError("Error: " + str(e))
else:
    printResult()


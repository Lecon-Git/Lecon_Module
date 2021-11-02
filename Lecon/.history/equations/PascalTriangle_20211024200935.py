#from . import spog
import spog


class Pascal:

    ###
    # TODO
    # This function compute a pascal expresion
    # (a + b)^n, where a -> 1st term, b -> 2nd term, and n -> power of the given equation
    # return the solution of the given binomial equation
    ###
    def __init__(self, firstTerm, secondTerm, index):
        ###
        # (a + b)^n
        # Argument:
        #   firstTerm (int) => a
        #   secondTerm (string) => b
        #   index (int) => n
        ###
        self.fTerm = firstTerm
        self.sTerm = secondTerm
        self.index = index + 1
        self.coefficients = []
        self.firstTermCollection = []
        self.secondTermCollection = []
        self.pascalSolutions = []

    def formatResult(self, arr):
        upBound = len(arr)
        for i in range(0, upBound):
            t = arr[i]
            if i != 0:
                if t[0] == "-":
                    arr[i] = " " + t[0] + " " + t[1:]
                else:
                    arr[i] = " + " + t[0:]
            print(arr[i], end="")

    def computeCoefficient(self):
        ###
        # argument:
        #   No argument
        # Return:
        #   list of coefficients
        ###
        index = self.index
        pascal_tree = list([[1], [1, 1], []])
        pascal_tree_len = len(pascal_tree)
        i = 2
        while(i < pascal_tree_len and pascal_tree_len <= index):
            for j in range(0, spog.add(i, 1)):
                if i < pascal_tree_len and j <= index:
                    if (j == 0 or j == i):
                        # append value 1 to the extreme sides of the list
                        pascal_tree[i].append(1)
                    else:
                        # append sum of the previous of the list to next of the element,
                        # to get immediate element of the list
                        pascal_tree[i].append(
                            spog.add(pascal_tree[i-1][j-1], pascal_tree[i-1][j]))
            #   Generically append an empty list if i a step less than pascal_tree length
            if (i == pascal_tree_len-1 and pascal_tree_len < index):
                pascal_tree.append(list())
                pascal_tree_len += 1
                i += 1
            else:
                i += 1

        self.coefficients = pascal_tree[index-1]  # store the last list.
        return self.coefficients

    def computeFirstTerm(self):
        term = self.fTerm
        self.firstTermCollection = [
            term**i for i in spog.reverseRange(self.index-1)]
        # return self.firstTermCollection

    def computeSecondTerm(self):
        term = self.sTerm
        if term.isdigit():
            return "Second term for this pascal module must be later. Try Again!"
        else:
            secondTermList = []
            if len(term) < 2 or len(term) > 2:
                return "Second term must not be 2 length, this must include the operator, + or -."
            else:
                op = 0
                if term[0] == "-":
                    op = -1
                else:
                    op = +1
                self.secondTermCollection = [
                    (op ** i, term[1]+"^"+str(i)) for i in spog.verseRange(self.index-1)]
        # return self.secondTermCollection

    def pascalSolution(self):
        ###
        # Final terms combine.
        # Here we combine both coefficient, first-term, and second-term values together.
        ###
        # call other functions here
        self.computeCoefficient()
        self.computeFirstTerm()
        self.computeSecondTerm()
        #
        coef = self.coefficients
        firstT = self.firstTermCollection
        secondT = self.secondTermCollection
        upBound = len(coef)

        combineCoefs = [(coef[i] * firstT[i] * secondT[i][0])
                        for i in range(0, upBound)]

        self.pascalSolutions = [str(combineCoefs[i]) + secondT[i][1]
                                for i in range(0, upBound)]

        return self.pascalSolutions

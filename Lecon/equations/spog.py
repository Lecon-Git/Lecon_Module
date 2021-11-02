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
import sys
import math
import random

###
# Validation of all entries should done at the frontend
###

# constant values
PIE = 3.1428571429
EXPO = 2.71828182845


def halt():
    sys.exit(1)


def exp(arg):
    return EXPO**arg


def addAllElements(arrayArg):
    ###
    # TODO
    # This function compute the sum of element in a given list of type integer
    # Takes a list argument
    # Return sum of all elements of the give list
    ###
    # Initialize sum variable
    sum = 0
    # look through the list and add on value to sum
    for i in arrayArg:
        sum += i
    # Return the result
    return sum


def add(arg1, arg2):
    ###
    # This function takes in two arguments and return their sum
    ###
    return arg1 + arg2


def multiply(arg1, arg2):
    ###
    # This function takes in two arguments and return their multiply
    ###
    return arg1 * arg2


def substract(arg1, arg2):
    ###
    # This function takes in two arguments and return their difference
    ###
    return arg1 - arg2


def divide(arg1, arg2):
    ###
    # This function takes in two arguments and return their division
    ###
    if arg2 == 0:  # Check for zeroerror
        return "Zero division error, check your denominator."
    return arg1 / arg2


def pythagoras(arg1, arg2, arg3, side="h"):
    ###
    # side could be either of these [hypotenuse: h, opposite: o, adjacent: a]
    ###
    answer = 0
    if side == "o":
        answer = sqrt(substract(square(arg3), square(arg1)))
    elif side == "a":
        answer = sqrt(substract(square(arg3), square(arg2)))
    else:
        answer = sqrt(add(square(arg1), square(arg2)))
    return answer


def sine(arg1, arg2):
    ###
    # sin of an angle = opp/hypo
    ###
    return float(arg1/arg2)


def cosine(arg1, arg2):
    ###
    # cos of an angle = adj/hypo
    ###
    return float(arg1/arg2)


def tan(arg1, arg2):
    ###
    # tan of an angle = opp/adj
    ###
    return float(arg1/arg2)


def cosecant(arg1, arg2):
    ###
    # cosec of an angle = hypo/adj
    ###
    return float(arg1/arg2)


def secant(arg1, arg2):
    ###
    # sec of an angle = hypo/opp
    ###
    return float(arg1/arg2)


def cotangent(arg1, arg2):
    ###
    # sec of an angle = adj/opp
    ###
    return float(arg1/arg2)


def maximum(arg1, arg2):
    ###
    # This function find maximum value between the two arguments supply
    ###
    if arg1 > arg2:
        return arg1
    elif arg2 > arg1:
        return arg2
    else:
        return "The numbers are equal!"


def minimum(arg1, arg2):
    ###
    # This function find minimum value between the two arguments supply
    ###
    if arg1 < arg2:
        return arg1
    elif arg2 < arg1:
        return arg2
    else:
        return "The numbers are equal!"


def generateRandomNumber(arg=999):
    ###
    # TODO
    ###
    return int(random.random() * arg) + 1


def areaOfCircle(arg):
    return PIE*square(arg)


def areaOfSquare(arg):
    return square(multiply(sqrt(2), arg))


def cube(arg):
    ###
    # TODO
    # This function compute square of a given integer
    # return square of the number
    return arg ** 3


def nth_index(arg1, arg2):
    ###
    # TODO
    # This function compute nth power of a given integer, n and where p is the power to which it raises
    # return square of the number
    return arg1 ** arg2


def sqrt(arg):
    ###
    # TODO
    # This function compute square of a given integer
    # return square of the number
    return arg ** 0.5


def cube_root(arg):
    ###
    # TODO
    # This function compute square of a given integer
    # return square of the number
    return arg ** (1/3)


def nth_root(arg1, arg2):
    ###
    # TODO
    # This function compute nth power of a given integer, n and where p is the power to which it raises
    # return square of the number
    return arg1 ** (1/arg2)


def square(arg):
    ###
    # TODO
    # This function compute square of a given integer
    # return square of the number
    return arg ** 2


def factorial(arg):
    ###
    # This function compute a factorial value of a given integer
    ###
    if (arg == 1) or (arg == 0):
        return 1
    ###
    # If n > 1 then compute its factorial
    ###
    return arg * factorial(arg-1)


def fibonacci(arg):
    ###
    # This function compute a fibonacci values
    ###
    if arg >= 0 or arg <= 2:
        sys.exit(1)
    ###
    # Initialize values indices 0, and 1
    ###
    values = [1, 1]
    for i in range(2, arg):
        # Add current element to the values data structure
        values.append(values[i-2] + values[i-1])
    return values

# Do this for the purpose of the below function - reverse range


def reverseRange(arg):
    # This include onset and the offset of the list generated. greater -> lesser
    i = 0
    while arg >= i:
        yield arg
        arg -= 1


def verseRange(arg):
    # This include onset and the offset of the list generated. greater -> lesser
    i = 0
    while i <= arg:
        yield i
        i += 1


def sigmoid(arg):
    ###
    # TODO
    # Implement Sigmoid Function
    # This takes in an argument of type integer
    # return a value range between 0 -> 1
    ###
    return 1 / (1+exp(arg))


def selectionSort(arrayArg):
    ###
    # TODO
    # Check if given arg is integer type or string
    # 0
    length = len(arrayArg)
    for i in range(length):
        for j in range(length):
            if arrayArg[i] > arrayArg[j]:
                pass
                print("#{} : {} ###".format(i, arrayArg))
    return arrayArg


def mergeSort(arrayArg):
    ###
    # TODO
    ###
    print("Merge sort function is not ready!")


def insertionSort(arrayArg):
    ###
    # TODO
    ###
    print("Insertion sort function is not ready!")


def linearSearch(arrayArg, key):
    ###
    # TODO
    # Compare key with every element in the given array
    # If equal to any element in the array supplied, return both element index
    # Else return -1 indicating that the is not in the array.
    ###
    for index, element in enumerate(arrayArg):
        if key == element:
            return index
    return -1  # return false if key not founds


def binarySearch(arrayArg, key):
    ###
    # TODO
    ###
    # sort
    #arrayArg = selectionSort(arrayArg)
    # Assuming the array is sorted
    length = len(arrayArg)
    first = 0
    last = length
    middle = (first+last)/2
    while(middle == 0 or middle == length):
        if key == arrayArg[middle]:
            return True
        elif key < arrayArg[middle]:
            last = middle
            middle = (first+last)/2
        elif key > arrayArg[middle]:
            first = middle
            middle = (first+last)/2

    return False


def isPositive(n):
    if(n > 0):
        return True
    else:
        return False


def isNegative(n):
    if(n < 0):
        return True
    else:
        return False


def toPositive(n):
    if not isPositive(n):
        n = n * (-1)
    return n

### This function takes in an arg... upon which numbers are yielded
### Here is a function which yield a range of numbers... This range takes into consideration
### both onset and the offset.
from math import spog

def my_range(x):
    i = 1
    while i <= x:
        yield i
        i += 1

def show():
    error = False
    try:
        x = int(input("Enter value for n range: ")) 
    except:
        print("Error: You've Entered Invalid Value. Try Again!")
        error = True
    finally:
        #if response is failure return
        if error:
            return
        #if response is success to the following
        for i in my_range(x):
            d = 10
            #logic for multiple of 10
            if i % d == 0:
                output = str(i) + " is a multiple of (" + str(d) + ") and its square is " + str(spog.square(i)) + ".\n"
                with open('output.txt', 'a') as f:
                    f.write(output)

show()
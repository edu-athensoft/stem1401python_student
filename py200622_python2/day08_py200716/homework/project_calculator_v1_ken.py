"""
For July 16th, 2020
Ken
Arithmetic and logical calculator
"""

# functions

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# make direct use of logic operations

def logicand(bool1, bool2):
    return bool1 and bool2

def logicor(bool1, bool2):
    return bool1 or bool2

def logicnot(bool1):
    return not bool1



# calculator

print("Arithmetic and logical calculator")

choice1 = input("Please write the number of the operation: \n"
                "1- add\n"
                "2- subtract\n"
                "3- multiply\n"
                "4- divide\n"
                "5- and\n"
                "6- or\n"
                "7- not\n: ")

if choice1 == "1":
    n1 = float(input("Please input the first value of the operation: "))
    n2 = float(input("Please input the second value of the operation: "))
    print(f"The sum of {n1} and {n2} is {sum(n1, n2)}")

elif choice1 == "2":
    n1 = float(input("Please input the minuend of the operation (minuend - subtrahend = difference): "))
    n2 = float(input("Please input the subtrahend of the operation: "))
    print(f"The difference of {n1} and {n2} ({n1} - {n2}) is {minus(n1, n2)}")

elif choice1 == "3":
    n1 = float(input("Please input the first factor of the operation: "))
    n2 = float(input("Please input the second factor of the operation: "))
    print(f"The product of {n1} and {n2} is {multiply(n1, n2)}")

elif choice1 == "4":
    n1 = float(input("Please input the divisor of the operation (divisor - dividend = quotient): "))
    n2 = float(input("Please input the dividend of the operation: "))
    print(f"The quotient of {n1} and {n2} is {divide(n1, n2)}")

elif choice1 == "5":
    bool1 = input("Please enter the first boolean: ")
    bool2 = input("Please enter the second boolean: ")
    print(f"{bool1} and {bool2} become {logicand(bool1, bool2)}")

elif choice1 == "6":
    bool1 = input("Please enter the first boolean: ")
    bool2 = input("Please enter the second boolean: ")
    print(f"{bool1} or {bool2} become {logicor(bool1, bool2)}")

elif choice1 == "7":
    bool1 = input("Please enter the  boolean: ")
    print(f"not {bool1} becomes {logicnot(bool1)}")

else:
    print("Wrong input, exit system")
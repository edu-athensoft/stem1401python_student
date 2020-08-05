"""
Error
    Syntax errors
    Logical errors (exception)

runtime, runtime error

Exception Handling makes program more robust
to avoid crushing caused by not fatal errors

1. pre-defined errors
2. user defined errors(exception)

"""


# type 1. error
# print(a)

# 1abc = 789

# if True:
#     print()
#   print()

# list1 = [1,2,3,4,5,6)

# tuple1 = (1,2,2,3,4,,5)


# type 2. logical error
# comment - addition
# num1 = input("number 1:")
# num2 = input("number 2:")
# res = float(num1) + float(num2)
# print(res)


# comment - concatenation
# num1 = input("number 1:")
# num2 = input("number 2:")
# res = num1 + num2
# print(res)


# FileNotFoundError
#

# ZeroDivisionError
# a = 9 / 0
# print(a)

# import math
# print(math.pi)


dict1 = {
    1: 11,
    2: 22
}

# dict1[3]
# count = 1
# while True:
#     print("infinite loop",count)
#     count += 1

import sys
count = 1
while True:
    print("infinite loop",count)
    count += 1
    if count == 10:
        sys.exit()

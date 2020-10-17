"""
define a function to calculate the cube of a number

How a function works in Python

"""

"""
step 1. define a function
  with one input parameter: number
  return cube of the number

step 2. specify a number to calculate

step 3. get and print out the returned value (result)
"""


def cube(a):
    return a * a * a

# def cube1(a):
#     res = a * a * a
#     return res


# main program
num = int(input("Put a number:"))

result = cube(num)

print("result = {}".format(result))



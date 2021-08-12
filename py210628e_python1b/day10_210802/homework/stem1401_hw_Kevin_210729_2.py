"""
write your docstring here

please write a program to get the product of
1x2x3x4x5x6x7x8x9x10

# 2x3x4x5x6x7x8x9x10X11

boundary
correct, completed

magic number
"""



# input and settings
N = 11

# constant
START = 2
STOP = N + 1

result = 1

for i in range(START, STOP):
    # print(i)
    result = result * i
    # print(result)

print("The product of the number sequence is {}.".format(result))
"""
list comprehension
"""

# matrix = []

matrix = [[i for i in range(3)] for i in range(3)]
print(matrix)

# create a 2d list
# 3x4
list2 = ['*' for i in range(3)]
print(list2)

list2 = [['*' for i in range(3)] for i in range(4)]
print(list2)


# 3*2*3
list3 = [[['*' for i in range(3)] for i in range(2)] for i in range(3)]
print(list3)


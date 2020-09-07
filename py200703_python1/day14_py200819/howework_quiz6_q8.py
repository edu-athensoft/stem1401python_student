"""

"""


# q8

"""
1   2   3   4
5   6   7   8
9   10  11  12
"""

# solution 1: hard code
print(1, end="\t")
print(2, end="\t")
print(3, end="\t")
print(4)
print(5, end="\t")
print(6, end="\t")
print(7, end="\t")
print(8)
print(9, end="\t")
print(10, end="\t")
print(11, end="\t")
print(12)
print("\n")

# solution 2: using variable
v1 = 15
v2 = 17
v3 = 60
v4 = 23

v5 = 32
v6 = 32
v7 = 58
v8 = 32

v9 = 79
v10 = 80
v11 = 94
v12 = 12

print(v1, end="\t")
print(v2, end="\t")
print(v3, end="\t")
print(v4)
print(v5, end="\t")
print(v6, end="\t")
print(v7, end="\t")
print(v8)
print(v9, end="\t")
print(v10, end="\t")
print(v11, end="\t")
print(v12)
print("\n")

# solution 3: using collection
numbers = (
    (1,2,3,4),
    (21,22,23,24),
    (31,32,33,34)
)

# print(numbers)
print(numbers[0],type(numbers[0]))
print(numbers[0][0], end="\t")
print(numbers[0][1], end="\t")
print(numbers[0][2], end="\t")
print(numbers[0][3])
print(numbers[1][0], end="\t")
print(numbers[1][1], end="\t")
print(numbers[1][2], end="\t")
print(numbers[1][3])
print(numbers[2][0], end="\t")
print(numbers[2][1], end="\t")
print(numbers[2][2], end="\t")
print(numbers[2][3])

# t1 = (1, 2, 3, 4)
# print(t1[0])
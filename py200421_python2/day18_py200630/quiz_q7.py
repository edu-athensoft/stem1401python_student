"""
union of sets
"""

# case 1. 2 sets
A = {1,2,3,4,5}
B = {1,2,3,4,6}

result = A | B
print(result)


# case 2. 3 or more sets
C = {11,22,33,44}
D = {55,66,77}

result = A | B | C
print(result)

result = A | B | C | D
print(result)


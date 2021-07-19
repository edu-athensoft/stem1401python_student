"""
isdisjoint()
"""

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {9,10}

#
result = A.isdisjoint(B)
print(result)

#
result = A.isdisjoint(C)
print(result)

# application

if A.isdisjoint(B):
    print("A and B have common items")
else:
    print("A and B do not have common items")


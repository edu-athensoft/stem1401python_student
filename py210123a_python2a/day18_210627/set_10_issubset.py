"""
issubset()

"""

A = {1,2,3}
B = {1,2}

# B
result = B.issubset(A)
print(result)

# C
C = {1,2,3}
result = C.issubset(A)
print(result)

# A
result = A.issubset(A)
print(result)



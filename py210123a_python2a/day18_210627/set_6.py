"""
Set operation
difference

"""

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Exclusive items in A
result = A - B
print(result)

# via function
result = A.difference(B)
print(result)

# ====================
# Exclusive items in B
result = B - A
print(result)

# via function
result = B.difference(A)
print(result)



"""
set operations
"""

# union
A = {1,2,3,4}
B = {5,6,7,8}

result = A | B
print(result)

A = {1,2,3,4}
B = {1,2,7,8}

result = A | B
print("A | B = ", result)

result = A.union(B)
print("A.union(B) = ",result)

result = B.union(A)
print("B.union(A) = ",result)

# intersection
A = {1,2,3,4}
B = {1,2,7,8}

result = A & B
print("A & B = ", result)

result = A.intersection(B)
print("A.intersection(B) = ",result)

result = B.intersection(A)
print("B.intersection(A) = ",result)


# difference
A = {1,2,3,4}
B = {1,2,7,8}

result = A - B
print("A - B = ", result)

result = A.difference(B)
print("A.difference(B) = ",result)

result = B - A
print("B - A = ", result)

result = B.difference(A)
print("B.difference(A) = ",result)



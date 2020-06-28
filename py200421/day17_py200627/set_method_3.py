"""
set method
issubset()

subset
"""

# case 1.
A = {1,2,3,4}
B = {1,2,3,4}

print("B.issubset(A) = ",B.issubset(A))
print("A.issubset(B) = ",A.issubset(B))
print()

# case 2.
A = {1,2,3,4}
B = {1,2,3}

print("B.issubset(A) = ",B.issubset(A))
print("A.issubset(B) = ",A.issubset(B))
print()


# case 3.
A = {1,2,3,4}
B = {1,2,3,5}

print("B.issubset(A) = ",B.issubset(A))
print("A.issubset(B) = ",A.issubset(B))


"""
issuperset()

the pattern of naming a boolean variable
"""

# case 1.

A = {1,2,3,4}
B = {1,2,3,4}

print("B.issuperset(A) = ",B.issuperset(A))
print("A.issuperset(B) = ",A.issuperset(B))
print()

# case 2.
A = {1,2,3,4}
B = {1,2,3}

print("B.issuperset(A) = ",B.issuperset(A))
print("A.issuperset(B) = ",A.issuperset(B))
print()

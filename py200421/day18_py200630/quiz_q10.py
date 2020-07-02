"""
issubset
issuperset
"""


# A = {1,2,3,4,5}
A = {1,2,3,4}
B = {1,2,3,4,6}

bool1 = A.issubset(B)
print(bool1)

bool2 = A.issuperset(B)
print(bool2)

bool2 = B.issuperset(A)
print(bool2)
"""
set symmetric difference

Symmetric Difference of A and B is a set of elements
in both A and B except those that are common in both.

"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

result = A ^ B
print(result)

result = A.symmetric_difference(B)
print(result)

result = B.symmetric_difference(A)
print(result)


# A - B | B - A
s1 = A - B
s2 = B - A
result = s1 | s2
print(result)


# A | B - (A & B)
s = A | B
c = A & B
result = s - c
print(result)







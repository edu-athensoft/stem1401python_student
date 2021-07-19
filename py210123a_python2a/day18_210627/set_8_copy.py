"""
set functions

copy a set

"""

# initialize A
A = {1, 2, 3, 4, 5}

# in order to maintain origin A, a copy of A is in need.

A2 = A.copy()

print('A',A, id(A))
print('A2',A2, id(A2))

print(A is A2)

#
A3 = A
print('A3',A3, id(A3))
print(A is A3)






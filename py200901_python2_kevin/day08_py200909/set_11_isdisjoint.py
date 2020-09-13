"""
set method

isdisjoint()
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# write a program to clarify the relationship between A and B
# if statement
is_disjoint = A.isdisjoint(B)

if is_disjoint:
    print("Set A and B are disjoint.")
else:
    print("Set A and B are not disjoint.")

"""
set - method
"""

# copy()
# copy a set and return


# is it a built-in function?
A = {1,2,3}

B = A.copy()
print(B)

print(B is A)


# isdisjoint()
print()
A = {1,2,3}
B = {4,5,6}
print("A is disjoint to B?",A.isdisjoint(B))


# subset and superset
A = {1,2,3}
B = {1,2,3}
B = {1,2}
B = {1,2,5}


print("A = ",A)
print("B = ",B)
print("B.issubset(A) ? ",B.issubset(A))

print("A.issuperset(B) ? ",A.issuperset(B))
print("B.issuperset(A) ? ",B.issuperset(A))


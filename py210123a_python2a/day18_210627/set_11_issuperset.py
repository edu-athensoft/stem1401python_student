"""
issuperset()

"""

A = {1,2,3}
B = {1,2}
C = {1,2,3}

# B
result = B.issuperset(A)
print(result)

#
result = A.issuperset(B)
print(result)

#
result = A.issuperset(C)
print(result)




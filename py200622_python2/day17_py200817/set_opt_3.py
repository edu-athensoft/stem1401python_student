"""
set operation - set difference

"""

A = {1,2,3,4}
B = {4,5,6,7}
print(f"Set A: {A}")
print(f"Set B: {B}")

result = A - B
print(f"Result Set A-B : {result}")

result = A.difference(B)
print(f"Result Set A-B : {result}")


result = B - A
print(f"Result Set B-A : {result}")

result = B.difference(A)
print(f"Result Set A-B : {result}")



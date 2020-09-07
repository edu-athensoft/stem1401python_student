"""
set operation - set symmetric difference

"""

A = {1,2,3,4}
B = {4,5,6,7}
print(f"Set A: {A}")
print(f"Set B: {B}")

result = A ^ B
print(f"Result Set A^B : {result}")

result = (A-B) | (B-A)
print(f"Result Set A^B : {result}")

result = (A | B) - (A & B)
print(f"Result Set A^B : {result}")

result = A.symmetric_difference(B)
print(f"Result Set A^B : {result}")

result = B.symmetric_difference(A)
print(f"Result Set A^B : {result}")



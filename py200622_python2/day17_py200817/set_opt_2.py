"""
set operation - set intersection

"""

A = {1,2,3,4}
B = {4,5,6,7}
print(f"Set A: {A}")
print(f"Set B: {B}")

result = A & B
print(f"Result Set: {result}")

result = A.intersection(B)
print(f"Result Set: {result}")

result = B.intersection(A)
print(f"Result Set: {result}")



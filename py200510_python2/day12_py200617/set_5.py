"""
Symmetric Difference
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

symdif = (A - B) | (B - A)
print(symdif)

result = A ^ B
print(result)

result2 = (A | B) - (A & B)
print(result2)
"""
Symmetric difference

(A - B) | (B - A)
"""

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

result = A.symmetric_difference(B)

result2 = B.symmetric_difference(A)

print(result)
print(result2)

# solution2
result3 = (A - B) | (B - A)
print(result3)




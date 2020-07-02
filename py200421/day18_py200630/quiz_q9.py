"""
symmetric difference
"""

#
A = {1,2,3,4,5}
B = {1,2,3,4,6}
C = {3,4,7}

result = A ^ B
print(result)


result = A ^ B ^ C
print(result)

result = C ^ B ^ A
print(result)

result = C ^ A ^ B
print(result)


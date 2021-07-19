"""
enumerate()
Return an enumerate object.
It contains the index and value of all the items of set as a pair.

"""

A = {'a','b','c'}
result = enumerate(A)
print(result)

result = list(result)

print(result)


#
result = enumerate(A, 10)
print(result)

result = list(result)

print(result)


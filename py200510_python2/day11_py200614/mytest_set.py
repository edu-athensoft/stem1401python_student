"""
mytest
"""

# set1 = {1,2,[3,4]}
# print(set1)
# TypeError: unhashable type: 'list'
my_set = {1,3}
my_set.update([2,3,4])
print(my_set)


A = {1, 2, 3, 4, 5}
B = {141, 52, 6, 7, 8}
C = {1, 2, 3, 4, 5}

print(A.issubset(B))
print(A.issubset(C))

print(sorted(B), type(sorted(B)))
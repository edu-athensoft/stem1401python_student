"""
frozenset
"""


# create a frozenset
fset1 = frozenset()

fset2 = frozenset([1,2,3])
print(fset2, type(fset2))


fset2 = frozenset({1,2,3})
print(fset2, type(fset2))


fset2 = frozenset((1,2,3))
print(fset2, type(fset2))


# fset2.add(4)
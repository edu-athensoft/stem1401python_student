"""
built-ins for set
"""

# all()
myset1 = {True, True, False, False, True, True}
print("All true?",all(myset1))

myset1 = set()
print("All true?",all(myset1))

print()


# any()
myset1 = {True, True, False, False, True, True}
print("Any true?",any(myset1))

myset1 = set()
print("Any true?",any(myset1))

print()

# len()
myset1 = {True, True, False, False, True, True}
print("len",len(myset1))


# max(), min()
set1 = {12,34,45,6,7}
print(max(set1), min(set1))

# sum()
set1 = {12,34,45,6,7}
print(sum(set1))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# set1 = {'ab','cd'}
# print(sum(set1))


# sorted()
result = sorted(set1)
print(result, type(result))
"""
set
A set is unordered collection of items

1. Unordered
2. Unique item
3. Set itself is mutable
4. The item in a set is immutable

"""

# create an empty set
# set1 = {}
set1 = set()
print(set1, type(set1))


# create a normal set
set2 = {1,2,3}
print(set2, type(set2))


# create a set with duplicated items
set3 = {'EUROPE','EUROPE','STAY HOME','STAY HOME','ASIA','ASIA','ASIA'}
print(set3)


# unordered
set4 = {'a','b','c'}
print(set4)


# immutable items
# set5 = {1,2,[5,6]} #TypeError: unhashable type: 'list'
# print(set5)

set5 = {1,2,(5,6)}
print(set5)

# set5 = {1,2,{5:'a',6:'b'}}  #TypeError: unhashable type: 'dict'
# print(set5)


# application
"""
how many places had thee students ever been?
A   US
B   EUROPE
C   ASIA
D   SOUTH AMERICA
E   AUSTRAILIA
F   STAY HOME
G   US
H   EUROPE
I   US
J   STAY HOME
K   ASIA
"""
"""
Python collection type:  List, Tuple, Set, Dict  (String)

A set is an unordered collection of items
Every element is unique
Set itself is mutable, items in the set are immutable
"""

# 1. understanding unordered structure
list1 = [1,2,3,5,3,4]
tuple1 = (1,2,3,5,3,4)

set1 = {1,2,3,1,2,3}
print(set1)

set2 = {'a','b','c'}
print(set2)


# 2. understanding unique item
set1 = {1,2,3,1,2,3}
print(set1)

set2 = {'a','b','c','b','c'}
print(set2)


# understanding mutable or immutable
set3={'abc','123',123,12.4, True, False}
print(set3)

set4 = {(1,2,3)}
print(set4)

# set5 = {[1,2,3],[1,2,3]}
# print(set5)

# set itself is mutable
set6 = {{1,2,3},4,5,6}
print(set6)





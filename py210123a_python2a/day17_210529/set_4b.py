"""
set
operation of removing items

discard()
remove()
pop() - removes an item arbitrarily from a set and returns that item
clear() - removes all items from a set
"""


set1 = {'red','blue','green'}
item = set1.pop()
print(item)

item = set1.pop()
print(item)

item = set1.pop()
print(item)

print("--------------")
set2 = {'red','blue','green'}
print(set2)

set2.clear()
print(set2)

print("--------------")
set3 = {'red','blue','green'}
print(set2)

# del set3
# print(set3)
# NameError: name 'set3' is not defined



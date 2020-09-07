"""
set

remove items from a set

discard() - remove a specified item
remove() - remove a specified item
pop() - remove an item randomly
clear() - remove all items

"""

# remove items by discard()
myset1 = {2, 3, 4, 5, 67, 7, 9, 45, 77, 51, 88, 91, 31}
myset1.discard(88)
print(myset1)

# myset1.discard()
# print(myset1)

myset1.discard(8888)
print(myset1)
print()


# remove items by remove()
myset1 = {2, 3, 4, 5, 67, 7, 9, 45, 77, 51, 88, 91, 31}
myset1.remove(88)
print(myset1)

# myset1.remove(88) # KeyError: 88
# print(myset1)

if 88 in myset1:
    myset1.remove(88)
    print(myset1)


# pop() - remove one item arbitrarily
myset1 = {'2', '3', '4', '5'}
myset1.pop()
print(myset1)

myset1.pop()
print(myset1)

# clear() - remove all items
myset1 = {'2', '3', '4', '5'}
myset1.clear()
print(myset1)






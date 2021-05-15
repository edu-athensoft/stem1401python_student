"""
set

mutable
change a set

add()
update()
"""

set1 = {1,2}
print(set1)

# can we get items from a set by index?
# result = set1[0]   # error
# TypeError: 'set' object does not support indexing


# add an item
set1.add(3)
print(set1)

# set1.add(3,4)
# print(set1)
# TypeError: add() takes exactly one argument (2 given)

set1.add((4,5))
print(set1)


print('=== add multiple items')
# add multiple items at a time
# update()
# update() accepts list,tuple,set, dict
set1.update([7,8,9])
print(set1)

set1.update((71,81,91))
print(set1)

set1.update([55,66,77],(11,12,13))
print(set1)

set1.update({33,44})
print(set1)

set1.update({'a':'aaa','b':'bbb'})
print(set1)

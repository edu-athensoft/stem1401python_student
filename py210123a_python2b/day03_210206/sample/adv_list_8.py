"""
list - remove items

remove()

pop()

clear()
"""

# remove() - remove the given item, delete by item

mylist = [1,2,3,44,5,6,7,8]
mylist.remove(44)
print(mylist)
print()

mylist = [1,2,3,44,5,6,44,7,8]
mylist.remove(44)
print(mylist)
mylist.remove(44)
print(mylist)

if 44 in mylist:
    mylist.remove(44)
print()


# pop() - remove an item by index
mylist = [1,2,3,44,5,6,7,8]
print(mylist.pop(3))
print(mylist)

# print(mylist.pop(9))
# print(mylist)
print()

# clear()
mylist = [1,2,3,44,5,6,7,8]
mylist.clear()
print(mylist)

# slicing []







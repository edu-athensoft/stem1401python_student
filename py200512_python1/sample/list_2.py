"""

"""
list5 = [1,2,34,6,6,67,7,8,8,9,9,'abc']

# remove() - delete by value (a given item)
list5.remove(34)
print(list5)

list5.remove(67)
print(list5)

list5.remove('abc')
print(list5)

# pop() - delete by index
list5 = [1,2,34,6,6,67,7,8,8,9,9,'abc']
list5.pop(0)
print(list5)


# remove all items
list5.clear()
print(list5)


# remove a part of a list - slicing
list5 = [1,2,34,6,6,67,7,8,8,9,9,'abc']
list5[1:6] = []
print(list5)


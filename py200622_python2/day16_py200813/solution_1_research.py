"""
# 1. Write a Python program to get a list, sorted in increasing order
# by the last element in each tuple from a given list of non-empty tuples.
# mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

expected result:  [(2, 1), (1, 2),(2, 3), (4, 4), (2, 5)]
"""


# research on sort()
mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
mylist.sort()
print(mylist)

# how to make the second item be the first item of the tuple

# convert to mutable type
tuple1 = (2, 1)
# myitem = list(tuple1)
# print(myitem)

# reverse items in the tuple
def swap(item):
    item = list(item)
    tmp = item[0]
    item[0] = item[1]
    item[1] = tmp
    return tuple(item)

print("After reversing: ",swap(tuple1))





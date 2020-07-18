"""
remove all items
keyword: del

"""

# case 1.
list1 = [1,2,3,4,5,6,7]
list1.clear()
print(list1)

# case 2.
# del - remove one item
list1 = [1,2,3,4,5,6,7]
del list1[0]
print(list1)

# del - remove multiple items
list1 = [1,2,3,4,5,6,7]
del list1[2:5]
print(list1)

# del - remove all items
list1 = [1,2,3,4,5,6,7]
del list1[:]
print(list1)

# del - remove all items along with the list object
list1 = [1,2,3,4,5,6,7]
del list1
print(list1)

#
list1 = [1,2,3,4,5,6,7]
print(list1[:])
print(list1)




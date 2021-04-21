"""

"""

# how to create
list1 = []
list2 = [1,2,3]
list3 = list(list2)     # clone
list4 = list3           # reference

# how to access items in a list
# by index
nested_list = [[1,2,3],[1,2,3],[1,2,3]]
print(nested_list[0][0])
# negative index

# slicing
list5 = [1,2,34,6,6,67,7,8,8,9,9]
print(list5[2:5])
print(list5[:5])
print(list5[5:])
print(list5[:])

# update element in a list
list5[0] = 999
print(list5)

list5[1:4] = [777,888,999]
print(list5)


# add elements
list5.append('abc')
print(list5)

list5.extend([123,123,123])
print(list5)

# +
list6 = [1,2,3]
list7 = [4,5,6]
print(list6 + list7)
print(list7 + list6)

# *
list6 = [1,2,3] * 3
print(list6)


# insert an item
list8 = [4,5,6]
list8.insert(1,9)
print(list8)

# insert items
list8[2:2] = [7,8,9]
print(list8)


# remove items
del list8[0]
print(list8)

del list8[1:3]
print(list8)


# del list8
# print(list8)

# clear()
list8.clear()
print("list8",list8)




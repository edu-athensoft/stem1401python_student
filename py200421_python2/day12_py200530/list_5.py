"""
list - append() and extend()
"""

mylist = [1,2,3,4,5,6]

# add 3 elements of 7,8,9
mylist.append(7)
print(mylist)

mylist.append(8)
print(mylist)

mylist.append(9)
print(mylist)

mylist.append(10)
print(mylist)


# add 3 items in one shot
mylist = [1,2,3,4,5,6]
mylist.extend([7,8,9])
print(mylist)

# add 'a','b','c' to [1, 2, 3, 4, 5, 6, 7, 8, 9]
# add 'a', 'b', 'c', to [1, 2, 3, 4, 5, 6 7, 8, 9]
mylist.extend(['a', 'b', 'c'])
print(mylist)











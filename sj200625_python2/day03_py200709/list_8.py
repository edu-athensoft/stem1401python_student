"""
Insert items

insert one item
insert one or more items

"""

# insert one item
odd = [1, 9]
print(odd)

# insert 3 between 1 and 9
# flexible
num = 7
odd.insert(1, num)
print(odd)

# hard code
# odd.insert(1,3)



# insert multiple items
odd = [1, 9]
# insert [3,5,7] into odd,   [1,3,5,7,9]
odd[1:1] = [3,5,7]
print(odd)

"""
list - insert(), slicing
"""

# insert() for one item
odd = [1, 9]

# insert the item of 3 at the index 1
odd.insert(1,3)
print(odd)


odd = [1, 9,10,11]

# insert the item of 3 at the index 1
odd.insert(1,3)
print(odd)


# insert values
odd = [1, 9]
odd[1:1] = [3,5,7]
print(odd)

# even = [2, 4, 10]
# even = [2,4,6,8,10]
even = [2, 4, 10]
even[2:1] = [6, 8]
print(even)

# even = [2, 4, 10]
# even = [2, 4, 6, 8, 10]
even = [2, 4, 10]
even[2:2] = [6, 8]
print(even)
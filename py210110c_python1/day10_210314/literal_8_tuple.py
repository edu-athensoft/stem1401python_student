"""
literal collection

tuple
similar to list
however, tuple is read-only
write-protected, safe


ordered
sequence

element, item
"""

# create a tuple
tuple1 = (2,4,6,8,10,12)
print(tuple1)

tuple2 = (4,6,2,8,10,12)
print(tuple1 == tuple2)

# access item
item = tuple1[5]
print(item)

# len()
length = len(tuple1)
print('length=', length)

#
# 'tuple' object does not support item assignment
# tuple1[5] = 14
# print(tuple1)

tuple1[5] = 12
print(tuple1)


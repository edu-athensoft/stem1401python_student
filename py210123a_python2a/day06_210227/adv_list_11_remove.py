"""
delete
remove items/elements
"""

odd = [1,2,3,5,7,9]

# del , remove one item
del odd[1]
print(odd)

# del, remove multiple items, slice
odd = [1,2,3,5,7,9,10,12,14]
del odd[6:]
print(odd)

# del, remove the entire list
del odd
# print(odd)

# empty a list
odd = [1,2,3,5,7,9,10,12,14]
odd.clear()
print(odd)


# remove() - delete item by value
print("remove()")
odd = [1,2,3,5,7,9,10,12,14,10]
odd.remove(10)
print(odd)

print("===")
# pop() - delete item by index
odd = [1,2,3,5,7,9,10,12,14]
odd.pop()
print(odd)

odd.pop()
print(odd)

odd.pop()
print(odd)

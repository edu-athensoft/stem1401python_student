"""
set

remove items

discard()
remove()
"""


set1= {1,3,4,5,6}
print(set1)


# discard an item
set1.discard(4)
print(set1)

# discard an item which does not exist
set1.discard(50)
print(set1)


print("=========")
set2= {1,3,4,5,6}
print(set2)

# remove an item
set2.remove(4)
print(set1)

# remove an item which does not exist
# KeyError: 50
# set2.remove(50)
# print(set1)
item = 50
if item in set2:
    set2.remove(item)
print(set2)

# or to apply exception handling

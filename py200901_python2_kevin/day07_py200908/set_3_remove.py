"""
remove items from a set
remove()
discard()
"""


my_set = {1, 3, 4, 5, 6}
print(my_set)

# remove items with discard()
my_set.discard(4)
print(my_set)

my_set.discard(4)
print(my_set)
print()


my_set = {1, 3, 4, 5, 6}
print(my_set)

# remove items with remove()
my_set.remove(4)
print(my_set)

# my_set.remove(4) # KeyError
# print(my_set)

target = 8
if target in my_set:
    my_set.remove(target)

print(my_set)








# set - remove items

my_set = {1,2,3,4,5,6,7,8,9}
print(my_set)

my_set.remove(2)
print(my_set)

# my_set.remove(2)    # KeyError
# print(my_set)

my_set.discard(3)
my_set.discard(3)

#
my_set.pop()
print(my_set)

my_set.pop()
print(my_set)

# clear
my_set = {1,2,3,4,5,6,7,8,9}
my_set.clear()
print(my_set)



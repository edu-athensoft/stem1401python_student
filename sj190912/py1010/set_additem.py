# set - adding item

# add a single item
my_set = {1,2,3,4,5,6}
my_set.add(7)
print(my_set)

# my_set.add(8,9) # error
# print(my_set)

# my_set.add(8)
# my_set.add(9)
# my_set.add(10)
# print(my_set)

# adding items in one shot
# update()
# my_set.update([8,9,10])
# print(my_set)

# my_set.update((8,9,10))
# print(my_set)

my_set.update({8,9,10})
print(my_set)

"""
update a set

add()
update()
"""

my_set = {1,3}
print("The original set is {}".format(my_set))

# add an item to a set
my_set.add(2)
print("The current set is {}".format(my_set))


# add multiple elements
# update()
# my_set.update(9,10)
# print(my_set)


# how to learn new things
my_set.update([9,10])
print(my_set)

my_set.update((5,6))
print(my_set)

my_set.update({'a','b'})
print(my_set)

my_set.update({'n','p'},['z','x'])
print(my_set)




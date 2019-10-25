# review datatype set
# set is unordered collection of items

# to create an empty set
my_set = set()
print(my_set, type(my_set))

my_dict = {}
print(my_dict, type(my_dict))

# add an item to a set
my_set.add('1')
print(my_set)

# add items to a set
my_set.update(['2','3','4'])
print(my_set)

my_list = [9]
my_set.update(my_list)
print(my_set)

# remove items from a set
# discard()
my_set.discard(9)
print(my_set)

my_set.discard(9)
print(my_set)

# remove()
my_set.remove('4')
print(my_set)

# my_set.remove(4)
# print(my_set)

# randomly remove an item
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())









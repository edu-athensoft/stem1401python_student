"""
remove elements from a set

discard()
remove()
pop()
"""


# discard()
my_set = {1, 3, 4, 5, 6}
print(my_set)


my_set.discard(1)
print(my_set)

my_set.discard(8)
print(my_set)
print()

# remove
my_set = {1, 3, 4, 5, 6}

my_set.remove(1)
print(my_set)

# my_set.remove(8)
print(my_set)
# KeyError: 8


# pop()
print("\n pop()")
my_set = {1, 3, 4, 5, 6}
my_set.pop()
print(my_set)

my_set.pop()
print(my_set)

my_set.pop()
print(my_set)

a = my_set.pop()
print(my_set, a, type(a))


my_set = {'1', '3', '4', '5', '6'}
my_set.pop()
print(my_set)

my_set.pop()
print(my_set)

my_set.pop()
print(my_set)

a = my_set.pop()
print(my_set, a, type(a))
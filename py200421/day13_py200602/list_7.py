"""
delete/remove element from a list
"""

# 1. del
my_list = ['p','r','o','b','l','e','m']

# remove one element
del my_list[2]
print(my_list)

# remove multiple elements
del my_list[1:5]
print(my_list)

# remove entire list
del my_list[:]
print(my_list)

# del my_list
# print(my_list)

# empty a list
my_list = ['p','r','o','b','l','e','m']
my_list.clear()
print(my_list)


# remove()
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list)

# my_list.remove('p')
# print(my_list)

my_list = ['p','r','o','p','l','e','m']
my_list.remove('p')
print(my_list)

my_list.remove('p')
print(my_list)


# pop()
my_list = ['p','r','o','p','l','e','m']
my_list.pop(0)
print(my_list)

my_list = ['p','r','o','p','l','e','m']
my_list.pop(3)
print(my_list)

my_list.pop()
print(my_list)

my_list.pop()
print(my_list)

# my_list.pop(30)
# print(my_list)


my_list = ['p','r','o','p','l','e','m']
my_list[2:5] = []
print(my_list)
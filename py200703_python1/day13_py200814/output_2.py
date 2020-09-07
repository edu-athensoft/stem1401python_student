"""
string.format()

using index

"""

# case 1. using index
friend1 = 'Marie'
option = 'afternoon'
print("Good {0}, {1}!".format(option, friend1))


# case 2.
breakfast1 = 'bread'
breakfast2 = 'milk'
breakfast3 = 'egg'
breakfast4 = 'bacon'

print("I love {} and {} for my breakfast!".format(breakfast1, breakfast2))
print("I love {0} and {1} for my breakfast!".format(breakfast1, breakfast2))
# reverse index
print("I love {1} and {0} for my breakfast!".format(breakfast1, breakfast2))

"""
String formatting
print()

positional parameter

"""

x = 5
y = 10

print("Here x is {}, and y is {}".format(x, y))

# index
print("Here y is {}, and x is {}. //error".format(x, y))

# solution 1 . adjust the order of input
print("Here y is {}, and x is {}".format(y, x))

# solution 2. adjust the index of placeholders
# important!
print("Here y is {1}, and x is {0}".format(x, y))





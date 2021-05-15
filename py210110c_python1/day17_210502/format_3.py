"""
String formatting
print()
format() by named parameter
"""

x = 5
y = 15
z = 25

# option 1.
print('Here x is {}, y is {}, z is {}.'.format(x, y, z))

# option 2.
print('Here x is {0}, y is {1}, z is {2}.'.format(x, y, z))
print('Here y is {1}, z is {2}, x is {0}.'.format(x, y, z))

# option 3.
print('Here y is {my_y}, z is {my_z}, x is {my_x}.'.format(my_x=x, my_y=y, my_z=z))

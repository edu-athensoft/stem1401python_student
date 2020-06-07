"""
tuple - change values
"""

my_tuple1 = (1, 2, 3, [41,42], 5, 6, 7, 8)
# TypeError: 'tuple' object does not support item assignment
# my_tuple1[0] = 99

my_tuple1[3][0] = 9
print(my_tuple1)


my_tuple2 = (1,2,3)
print(my_tuple2)

# +
my_tuple = my_tuple1 + my_tuple2
print(my_tuple)

# *
my_tuple = my_tuple2 * 3
print(my_tuple)
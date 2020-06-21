"""
tuple - slicing
"""

my_tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)

# in the middle
print(my_tuple1[2:5])

# from the start
print(my_tuple1[:5])

# to the end
print(my_tuple1[2:])
print(my_tuple1[2:8])

# pay attention to this case
print(my_tuple1[2:-1])  # not work properly, lost the last item
print(my_tuple1[-1])
# print(my_tuple1[2:0]) # does not work

print(my_tuple1[5:2])


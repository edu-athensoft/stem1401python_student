"""
tuple
read-only list
"""

# create a tuple
my_tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(my_tuple1)

my_tuple2 = ()
print(my_tuple2)

# create a tuple with only one element
my_tuple3 = (1)
print(my_tuple3)
my_tuple3 = ('abc')
print(my_tuple3)
my_tuple3 = 1
my_tuple3 = (1,)
print(my_tuple3)

# create nested tuple
my_tuple4 = (1, 2, 3)
print(my_tuple4)
my_tuple4 = (('a','b'), 2, ('c','d'))
print(my_tuple4)
my_tuple4 = (('a','b'), ('c','d'), ('c','d'))
print(my_tuple4)

# create mix tuple
my_tuple5 = (['a','b'], ('c','d'), ('c','d'))
my_tuple5 = (['a','b'], ([1,2],'d'), ('c','d'))

# compare
# student profile collection
# pre-set scouting path
a = [(), (), ()]

# saving-slot in a game
b = ([], [], [])


# create a tuple by auto-packing
my_tuple = 1,2,'a'
print(my_tuple)

# unpacking
x, y, z = my_tuple
print(x)
print(y)
print(z)

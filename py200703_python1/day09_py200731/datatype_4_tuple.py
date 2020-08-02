"""
tuple

"""

# tuple is immutable (unchangeable)
# read-only
# write-protected
# ordered sequence

# create
tuple1 = (1,2,3,4,1,2,33)

# create an empty tuple
tuple2 = ()
print(tuple2, type(tuple2))

# create a tuple with only one item
list1 = [9]
tuple3 = (8)
print(tuple3, type(tuple3))
tuple3 = (8,)
print(tuple3, type(tuple3))

# index
print(tuple1[0])
print(tuple1[-1])
print(tuple1[len(tuple1)-1])

# tuple slicing
print(tuple1[0:3])

"""
Changing a Tuple

tuples are immutable
"""

tuple1 = (1,2,3)

# 1
# 2 -> 20
# TypeError: 'tuple' object does not support item assignment
# tuple1[1]=20
print(tuple1)


# 2
tuple2 = (1,[2],3)
tuple2[1][0]=20
print(tuple2)


# 3. reassign
t1 = (1,2,3)
t1 = (2,3,4)
print(t1)


# 4. change items by programming
"""
tuple -> list
change
list -> tuple
"""
# change an item of a tuple
# 5 -> 50    (4, 50, 6)
tuple3 = (4,5,6)
print(tuple3)

# convert a tuple to a list
list3 = list(tuple3)
print(list3)

# change

# convert the list back to a tuple





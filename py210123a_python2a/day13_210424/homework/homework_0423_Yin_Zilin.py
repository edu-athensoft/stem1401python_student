"""
1. Write a Python program to convert a list to a tuple.
2. Write a Python program to remove an item from a tuple.
3.Write a Python program to add an item in a tuple.
Hints:
list(collection_object) - convert collection_object to a list
tuple(collection_object) - convert collection_object to a tuple
4. Write a Python program to convert a tuple to a string.
"""

# 1

list1 = [1,2,3,4]
print(tuple(list1))

# 2
tuple1 = [1,2,3,4]
del tuple1[0]
print(tuple1)
print(type(tuple1))

# 3

tuple2 = [1,2,3,4]
list2 = list(tuple2)
list2.append(5)
print(tuple(list2))

# 4

tuple3 = [1,2,3,4]
print(str(tuple3))



# solution. 2
tuple1 = (1,2,3,4)
list1 = list(tuple1)
del list1[0]
print(tuple(list1))


# solution 4.
#rewrite

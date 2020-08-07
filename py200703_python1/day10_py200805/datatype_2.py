"""
datatype conversion - collection types
"""

# list -> tuple
list1 = [1,2,3]
res = tuple(list1)
print(res, type(res))

# tuple -> list
tuple1 = (1,2,3)
res = list(tuple1)
print(res, type(res))

# list -> set
list1 = [1,2,3,1,2,3]
res = set(list1)
print(res, type(res))

# set -> list
set1 = {1,2,3}
res = list(set1)
print(res, type(res))

# tuple -> set
# set -> tuple

# list, nested list
nested_list = [[1,11],
               [2,22],
               [3,33]]

print(nested_list)
dict1 = dict(nested_list)
print(dict1, type(dict1))

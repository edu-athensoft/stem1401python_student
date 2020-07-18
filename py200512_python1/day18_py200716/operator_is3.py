"""
is, is not

"""

# collection datatype
# list, tuple, set, dict

# case 1. list
list1 = [1,2,3]
list2 = [1,2,3]

print(list1==list2)
print(list1 is list2)
print()

# case 2. tuple
tuple1 = (1,2,3)
tuple2 = (1,2,3)

print(tuple1 == tuple2)
print(tuple1 is tuple2)
print()

# case 3. set
set1 = {1,2,3}
set2 = {1,2,3}

print(set1==set2)
print(set1 is set2)
print()

# case 4. dict
dict1 = {1:'a',2:'b',3:'c'}
dict2 = {1:'a',2:'b',3:'c'}

print(dict1==dict2)
print(dict1 is dict2)
print()

print(dict1 is not dict2)

# not is
# is not
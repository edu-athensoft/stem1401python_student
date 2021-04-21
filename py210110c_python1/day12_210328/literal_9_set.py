"""
literal set

What is set in python?
Set is an unordered collection of items

Set cannot contain duplicated items.

"""


# create a set
set1 = {1,2,3,4,5,6}
print(type(set1))

# create an empty set
set2 = set()
print(type(set2))

# unordered collection
set3 = {'a','b','c'}
print(set3)

# output
# {'b', 'c', 'a'}
# {'b', 'c', 'a'}
# {'b', 'a', 'c'}
# {'b', 'a', 'c'}
# {'c', 'a', 'b'}
# {'c', 'b', 'a'}
# {'a', 'c', 'b'}

# unique item
set4 = {1,2,3,4}
print(set4)

set5 = {1,1,2,2,3,3,4,4}
print(set5)



"""
list - slice
from middle to the right most

syntax
list_name[]
list_name[]

"""

list1 = ['a','b','c','d','e']

# solution 1. hard code
# d,e
res = list1[3:5]
print(res)

# no error
res = list1[3:8]
print(res)


# solution 2. calculate the index of last item
res = list1[3:len(list1)]
print(res)

# solution 3.
res = list1[3:]
print(res)



"""
list - slice
from left most

syntax
list_name[0:pos]
list_name[:pos]

"""

list1 = ['a','b','c','d','e','f','g','a','b','c','d','e','f','g']

# a,b,c,d
res = list1[0:4]
print(res)

# a,b,c,d,e
res = list1[0:5]
print(res)

# a,b,c
res = list1[0:3]
print(res)


#
res = list1[:3]
print(res)


# from the index of 0 to the one before the last one
res = list1[:13]
print(res)

# hint: negative index
res = list1[:-1]









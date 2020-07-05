"""
slicing
"""

mylist = ['a','b','c','d','e','f']
print(mylist[1:5])
# b,c,d
print(mylist[1:4])
# d,e
print(mylist[3:5])
print(mylist[-3:-1])


# slicing from 0
print(mylist[0:4])
print(mylist[:4])
# a,b,c
print(mylist[:3])
# a,b,c,d,e
print(mylist[:5])

# slicing till end
print(mylist[2:])
# d,e,f
print(mylist[3:])
# b,c,d,e,f
print(mylist[5:])

# slicing all, from start to end
print(mylist[:])
print(mylist)

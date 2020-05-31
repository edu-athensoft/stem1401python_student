"""
list - change values in a list
"""

# change value
odd = [2, 4, 6, 8]

odd[0] = 1
print(odd)

# change values
odd[1:4] = [3,5,7]
print(odd)


# ['a','b','c','d','e']

# Issa ['a1','b1','c1','d1','e']
# ['a', 'b', 'c', 'd', 'e']
mylist = ['a', 'b', 'c', 'd', 'e']
mylist[0:4] = ['a1', 'b1', 'c1', 'd1']
print(mylist)

# Zihan ['a','b2','c2','d2','e']
mylist = ['a', 'b', 'c', 'd', 'e']
mylist[1:4] = ['b2', 'c2', 'd2']
print(mylist)


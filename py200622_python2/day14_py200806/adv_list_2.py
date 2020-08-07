"""
slicing
"""

mylist = ['a','b','c','d','e','f','g','h']

# case 1. from 0..('e')
print(mylist[0:5])
print(mylist[:5])
print()

# case 2. from ('f')..end
print(mylist[5:len(mylist)-1+1])
print(mylist[5:8])
print(mylist[5:-1]) # error
print(mylist[5:])

# case 3. from ('c')..('f')
print(mylist[2:6])

# case 4.
print(mylist[:])


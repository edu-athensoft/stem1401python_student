"""
quiz5
"""

bool1 = True
print(bool1, type(bool1))

print(isinstance(bool1, int))


# f1 is a floating number
f1 = 1.23
print(f1, type(f1))

#
num = 9
print(isinstance(num, int))


# 6.2
mylist = [2,6,3,1,0,7]
print(mylist[0])
print(mylist[-1])
print(mylist[5])

# 6.3
mylist[3] = 999
print(mylist)
print()

# 6.4
mytuple = (2,6,3,1,0,7)
print(mytuple[0])
print(mytuple[5])

# 6.5
# mytuple[3] = 999

# 6.6
myset = {1,1,2,2,3,3}
print(myset)

# 6.7
mydict = {
    1:"Mon",
    2:"Tue"
}
print(mydict)

# 7
a1 = 1.2
b1= str(a1)
print(b1, type(b1))

# ValueError: invalid literal for int() with base 10: '1.2'
b1 = '3'
c1 = int(b1)
print(c1, type(c1))
print()

# convert string into float
a1 = '1.2'
b1 = float(a1)
print(b1)

# convert float to int
c1 = int(b1)
print(c1, type(c1))


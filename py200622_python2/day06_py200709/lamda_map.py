"""
lambda map()
"""

# original list
mylist = [1,2,3,4,5,6,7]

# generate a new list based on the original one
# new item = square of item (item**2)
a = map(lambda x: x**2, mylist)
print(a, type(a))

# extract data from map
b = list(a)
print(b, type(b))



# ex - 1
# generate a new dataset based on the given one using map() and lambda
dataset = ['a','b','c']

# expected
# newdataset = [97,98,99]

# ken - mapping
c = map(lambda y: ord(y), dataset)
d = list(c)
print(d)


# max
c = map(lambda x: ord(x), dataset)
print(list(c))

# kevin
c = map(lambda x: ord(x), dataset)
d = list(c)

# extract data from map
print(d, type(d))


# neilson
a = map(lambda x: ord(x), dataset)
print(list(a))

# yixuan
a = map(lambda x: ord(x), dataset)

# steven
x = map(lambda y: ord(y), dataset)
f = list(x)
print(f)







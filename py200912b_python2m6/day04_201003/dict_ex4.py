"""
combine 2 lists into one dictionary

zip()
"""

list1 = [0,   1,  2,  3,  4,  5]
list2 = ['a','b','c','d','e','f']


mydict = {}

for i in list1:
    mydict[i] = list2[i]

print(mydict)


# combine 2 lists

list3 = [10,   11,  12,  13,  14,  15]
list4 = ['a',  'b', 'c', 'd', 'e', 'f']
mydict = {}

for i in range(6):
    mydict[list3[i]] = list4[i]
print(mydict)


# combine 2 lists using zip()
# dict()
mydict = dict(zip(list3, list4))
print(mydict)
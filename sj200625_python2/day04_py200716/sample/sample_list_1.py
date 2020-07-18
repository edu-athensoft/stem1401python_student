"""
index()

the first index
the second index
"""

mylist = [3, 8, 1, 6, 0, 8, 4, 3, 8, 1, 6, 0, 8, 4]

# the 1st index
i1 = mylist.index(8)
# print("i1",i1)

# the 2nd index
# i2 = mylist.index(8,i1+1,-1)
i2 = mylist.index(8,i1+1)
# print("i2",i2)

# find all
i1 = -1

while i1+1<=len(mylist):
    if 8 in mylist[i1+1:]:
        i = mylist.index(8, i1+1)
        i1 = i
        print(i)
    else:
        break

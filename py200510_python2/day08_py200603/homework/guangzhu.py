mylist = [3, 8, 1, 6, 0, 8, 4]
mylist.pop(1)
mylist.insert(2,1)
target = 8
if target in mylist:
    print(mylist.index(target))
else:
    print(None)


#
mylist = [3, 8, 1, 6, 0, 8, 4]
indexes = [index for index in range(len(mylist)) if mylist[index] == 8]
print(indexes)
"""


"""


def swap(item):
    item = list(item)
    tmp = item[0]
    item[0] = item[1]
    item[1] = tmp
    return tuple(item)

mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
swaplist = []

# reverse each item of tuple in the mylist
for i in mylist:
    swaplist.append(swap(i))

print("swaplist", swaplist)

swaplist.sort()

print("sorted swaplist", swaplist)

resultlist = []
for i in swaplist:
    resultlist.append(swap(i))

print("resultlist", resultlist)

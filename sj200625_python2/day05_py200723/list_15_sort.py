"""
list.sort() - sort items in a list in ascending order
the descending order

view data
min, max
"""

list1 = [3,5,3,6,8,3,7,9,0,3,4,7]

# asc
list1.sort()
print(list1)

print("the max num is {}".format(list1[-1]))
print("the min num is {}".format(list1[0]))

# desc
list1.sort(reverse=True)
print(list1)
print("the max num is {}".format(list1[0]))
print("the min num is {}".format(list1[-1]))


# asc
list2 = ['bcd','ab','bc','a','bce']
list2.sort()
print(list2)

# list2 = ['bcd','ab','bc','a','bce','',None]
# list2.sort()
# print(list2)


# list2 = ['bcd','ab','bc','a','bce','',0,9]
# list2.sort()
# print(list2)

list2 = ['bcd','ab','bc','a','bce','','0','9','Z','A']
list2.sort()
print(list2)






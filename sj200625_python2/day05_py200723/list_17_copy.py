"""
list copy() - clone
"""

list1 = [1,2,3]
print("list1 = {}".format(list1))

list2 = list1.copy()
print("list2 = {}".format(list2))

print(list1 is list2)

list1[0]= list1[0] * 10
print("list1",list1)
print("list2",list2)



#
list3 = list1
print(list3 == list1)
print(list3 is list1)
print(list1)
print(list3)



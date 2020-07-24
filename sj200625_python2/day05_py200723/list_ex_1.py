"""
Write a Python program to remove duplicates from a list
"""

list1 = [1,1,2,1,2,3,2,3,1,4,4]
list2 = []

for x in list1:
   if x not in list2:
       list2.append(x)

print(list2)


# option 2.
list2 = list(set(list1))
print(list2)


# youran
list1 = [1, 1, 2, 2, 3, 3, 4, 4]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        list1.remove(i)
print(list2)
print(list1)


# leon
# for x in list1:
#     if x in list1*2:
#         list1.pop(x)
#
# print(list1)




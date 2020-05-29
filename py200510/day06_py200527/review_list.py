"""
clone or copy lists
"""

list1 = [1,2,3]

# list2 = list1

# list()
list2 = list(list1)

# for-loop
list2 = []
for i in list1:
    list2.append(i)
print(list2)

print(list1 == list2)
print(list1 is list2)



"""
list comprehension
"""

list1 = [1,2,3,4,5]
# list2 = [2,4,6,8,10]

# by iteration
list2 = []
for i in list1:
    list2.append(i*2)

print(list2)

# map, lambda
list2 = list(map(lambda x: 2*x, list1))
print(list2)

#
list2 = [2*x for x in list1]
print(list2)

# list3 = [1,4,9,16,25]
list3 = [x**2 for x in list1]
print(list3)

# list4 = [1,9,25]
list4 = [x**2 for x in list1 if x % 2 == 1]
print(list4)





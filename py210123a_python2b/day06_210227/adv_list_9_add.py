"""
add items

list is mutable (changeable)
"""


list1 = ['a','b','c','d','e']
print(list1)

# add one item
# append()
list1.append('f')
print(list1)

myitem = 'g'
list1.append(myitem)
print(list1)

print("===")
# add multiple items
list1 = ['a','b','c','d','e']

# add 'f' and 'g'
# extend()
mylist = ['f','g']
list1.extend(mylist)
print(list1)

#
list1 = ['a','b','c','d','e']
list1.extend(['f','g'])
print(list1)
print("===")

# + operator
list1 = [1,3,5]
list2 = [2,4,6]
list3 = list1+list2
print(list3)

list4 = list2+list1
print(list4)

# * operator
list5 = list1 + list1 + list1 + list1
print(list5)

list5 = list1 * 5
print(list5)




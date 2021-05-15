"""
1. Write a Python program to remove duplicates from a list.
2. Write a Python program to check a list is empty or not
3. Write a Python program to clone or copy a list.
"""

# 1

list1 = ['a','a','a','b','b','b','c','c','c']
print(list1)
list2 = []

for items in list1:
    if items not in list2:
        list2.append(items)

print(list2)

print()

# 2

list3 = ["asdf"]

for items in list3:
    if items == []:
        print("the list is empty")
    else:
        print("this list is not empty")

print()

# 3

list4 = ['a','b','c']

clone = list4

print(clone)




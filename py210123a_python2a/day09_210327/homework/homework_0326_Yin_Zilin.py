"""
1. Write a Python program to generate a 3*2*3 3D array whose each element is *.
2. Write a Python program to shuffle and print a specified list.
Hint:
You may search on Internet with the keywords like 'python list shuffle'
3. Write a Python program to get the difference between the two lists.
"""

# 1


# 2

import random

list1 = ['1','2','3','4','5']

random.shuffle(list1)

print("The shuffled list is ",list1)

# 3

list2 = ['a','b','c']
list3 = ['a','d','f']
list4 = list2 + list3

result = []

for i in list4:
    if list4.count(i) < 2:
        result.append(i)

print("The list consisting of different items is ",result)
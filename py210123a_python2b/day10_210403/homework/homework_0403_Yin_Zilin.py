"""
1. Write a Python program to generate a 3*4 2D array whose each element is *.
2. Write a Python program to generate a 3*2*3 3D array whose each element is *.
Hints:
The list comprehension should be applied to question 1 and 2.
3. Select all odd numbers from a list.
Hints:
Please generate a list with numbers ranging from 1 to 50, and then shuffle it.
Using filter of list comprehension
"""

# 1

arr1 = []

x = 3

for i in range(x):
    arr1.append('*')

arr2 = []

y = 4

for i in range(y):
    arr2.append(arr1)

print(arr2)

# 2

arr3 = []

x = 3

for i in range(x):
    arr3.append('*')

arr4 = []

y = 2

for i in range(y):
    arr4.append(arr3)

arr5 = []

z = 3

for i in range(z):
    arr5.append(arr4)

print(arr5)

# 3

import random

list1 = []
list2 = []

for i in range(1,51):
    list1.append(i)

random.shuffle(list1)
print(list1)

for o in list1:
    if o %2 == 1:
        list2.append(o)

print(list2)
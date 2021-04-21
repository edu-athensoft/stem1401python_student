"""
1. Write a Python program to sum all the even numbers in a list.
"""

list1 = [1,2,3,4,5,6,7,8,9]

result = 0

for items in list1:
    if items % 2 == 0:
        result += items

print(result)


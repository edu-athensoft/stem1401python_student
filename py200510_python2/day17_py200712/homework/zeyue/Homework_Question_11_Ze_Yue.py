"""
7/11/2020
Ze Yue Li
[Homework]
11. Write a Python program to multiply all the items in a dictionary.
"""

#  sum -> product

dict3 = {5:50, 6:60, 7:70, 8:80, 9:90}
sum = 1
for i in dict3:
    sum = sum * dict3[i]
print(dict3)
print(sum)
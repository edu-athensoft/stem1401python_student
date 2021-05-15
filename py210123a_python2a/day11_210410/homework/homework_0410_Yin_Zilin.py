"""
1. Write a program to generate a list.
selecting all even numbers from 1 to 100, and then generate a list in which each item is square of the corresponding even number.
Hints: Using list comprehension
Sample: [1,2,3,4,5,6,7,...100]
Expected Result: [ 4, 16, 36, 64, 100, ... , 10000]

2. Write a program to generate a list.
There are two given string 'ABC' and 'XYZ'
generating a new list like ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
Hints: Using list comprehension
"""

# 1

list1 = []

for i in range(1,101):
    list1.append(i)

print(list1)

result = [i**2 for i in list1 if i %2 == 0]
print(result)

# 2
# linear algebra
string1 = 'ABC'
string2 = 'XYZ'
result = []

for i1 in string1:
    for i2 in string2:
        print(i1+i2)
        result.append(i1+i2)

print(result)
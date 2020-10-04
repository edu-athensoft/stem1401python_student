"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a program to sort a dictionary by value
in both ascending and descending order.

Hints:
sorted()
lambda function
dict.items()
dict()
"""

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_d)

# lambda x:  2*x+1

# lambda item: item[1]
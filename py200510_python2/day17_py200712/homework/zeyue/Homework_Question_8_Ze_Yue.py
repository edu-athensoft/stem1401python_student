"""
7/11/2020
Ze Yue Li
[Homework]
8. Write a Python script to merge two Python dictionaries.
"""
dict1 = {1: 5, 2: 6, 3: 7}
dict2 = {4: 8, 5: 9, 6: 10}

dict1.update(dict2)
print(dict1)
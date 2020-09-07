"""
2. Write a Python program to count the number of characters (character frequency) in a string.

Sample String : 'google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

5 min
"""

"""
string.count()
efficiency
"""

str1 = 'google.com'
set1 = set(str1)

# print(set1)

for char in set1:
    print(f"{char}: {str1.count(char)}")




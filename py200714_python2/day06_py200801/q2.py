"""
2. Write a Python program to count the number of characters
(character frequency) in a string.
Sample String : 'google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

"""
t1 = (1,2,1,2,1,2)
print(t1)

s1 = {1,1,2,2,3,3}
print(s1)
"""

str1 = 'google.com'

dict1 = {}

for char in str1:
    # print(char)
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1

print(dict1)



"""
Count String
"""
"""
str_1 = input("Input a string: ")
set_1 = set(str_1)
print(set_1)
for i in set_1:
    print(f"{i}: {str_1.count(i)}")
    
str_2 = input("Input a string: ")
dict_1 = {}
for char in str_2:
    print(char)
    if char in dict_1:
        dict_1[char] += 1
    else:
        dict_1[char] = 1
print(dict_1)
"""
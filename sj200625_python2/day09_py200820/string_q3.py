"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given
a string. If the string length is less than 2, return instead of the empty string.

Sample String : 'w3resource'
Expected Result : 'w3ce'

Sample String : 'w3'
Expected Result : 'w3w3'

Sample String : 'w'
Expected Result : 'Empty String'

5 min

"""

str1 = 'w3resource'
# str1 = 'w'

if len(str1) >= 2:
    first2 = str1[:2]
    last2 = str1[-2:]
    # print(first2,last2)
    result = first2 + last2
else:
    result = 'Empty String'

print(result)





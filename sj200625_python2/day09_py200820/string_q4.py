"""
4. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first
char itself.

Sample String : 'restart'
Expected Result : 'resta$t'

4 min

"""

"""
replace()
"""

str1 = 'restart restart'
fchar = str1[0]
result = fchar + str1[1:].replace(fchar,'$')
print(result)


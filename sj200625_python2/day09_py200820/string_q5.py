"""
5. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

3 min
"""

string1 = "abc"
string2 = "xyz"

# string1 = "ab"
# string2 = "xy"

if len(string1) >=2 and len(string2) >=2:
    string3 = string1[:2] + string2[2:]
    string4 = string2[:2] + string1[2:]
    print(string4 + " " + string3)
else:
    print("Cannot do it")

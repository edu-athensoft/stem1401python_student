"""
String
A string is actually a tuple
access a char in a string
slicing - list,tuple,string
"""


string1 = "abcdef"

# access a char
# via index starting from 0

# 1st char
char1 = string1[0]
print(char1)

# the last char
char2 = string1[-1]
print(char2)


# slice - get a substring
# get 'bcd'
s1 = string1[1:4]
print(s1)

s2 = string1[:4]
print(s2)

s3 = string1[2:]
print(s3)


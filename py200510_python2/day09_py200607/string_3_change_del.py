"""
string - change or delete
"""

str1 = "athensoft inc."
print('str = ', str1)

# changing char(s) in a string
# TypeError: 'str' object does not support item assignment
# str1[0] = 'A'


# reassign is allowed
str1 = "Athensoft Inc."
print(str1)



# delete char(s) from a string
# TypeError: 'str' object doesn't support item deletion
# del str1[-1]

# allowed
del str1       # works

# NameError: name 'str1' is not defined
print(str1)


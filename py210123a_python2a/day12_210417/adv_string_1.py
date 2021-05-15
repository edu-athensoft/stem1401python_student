"""
string

A string is a sequence of characters.
char = alphabet, digit, symbol, punctuation

immutable

discovery
C - string is not a primitive type
Java - string is reference type
"""


# create a string
str1 = 'hello'
print(str1)

# string v.s. tuple
# immutable, ordered
('h','e','l','l','o')



# use a string as a tuple
# access element (char)
print(str1[0])
print(str1[-1])

# slice
str2 = str1[1:3]
print(str2)

# length
print(len(str1))
print(len(str2))

# change a string
# TypeError: 'str' object does not support item assignment
# str1[0] = 'H'   # h -> H

# reassign
str2 = 'abc'
print(str2)


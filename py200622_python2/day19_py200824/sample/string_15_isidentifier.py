"""
isidentifier()

returns True if the string is a valid identifier in Python. If not, it returns False.

string.isidentifier()

"""

# Example 1
str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '22Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())

str = '_123'
print(str.isidentifier())

str = '__abc__'
print(str.isidentifier())

str = '_'
print(str.isidentifier())

_ = 123
print(_)
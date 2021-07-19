"""
input and data type

raw input is of 'str' type
"""

num = input('Enter a number of Integer:')

# TypeError: can only concatenate str (not "int") to str
# result = num + 2
# str + int

# ValueError: invalid literal for int() with base 10: '4.2'
# result = int(num)+2


result = float(num)+2

print(type(num))
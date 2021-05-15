"""
String
index()

if not found, an error occurs.
"""

str1= "abc abc abd bcd bca"

pos = str1.index('abc')
print(pos)

# ValueError: substring not found
pos = str1.index('xyz')
print(pos)


if pos == str1.find('xyz'):
    pass
else:
    pass


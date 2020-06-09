"""
string - enumerate()
"""

mystr = 'hello world'
print(mystr)

a = enumerate(mystr)
print(a, type(a))

print(list(a))
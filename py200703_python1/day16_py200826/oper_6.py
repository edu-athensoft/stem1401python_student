"""
special operator

identity operator       - is, is not
membership operator     - in, not in

"""

x = 1
y = 1
print(x is y)

x = 'a'
y = 'a'
print(x is y)
print()

x = [1,2,3]
y = [1,2,3]
print(x is y)
print(x == y)

print()
x = (1,2,3)
y = (1,2,3)
print(x is y)
print()

# membership
x = [1,2,3]

print(4 in x)
print(4 not in x)

print(1 in x)
print(1 not in x)

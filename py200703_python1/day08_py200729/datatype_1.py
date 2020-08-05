"""
datatype
Knowing Datatype, then knowing the operations on the data

Every value in python has a datatype

Numbers (int, float, complex)

"""

# type() - built-in function in python

a = 10
print(a, type(a))

# integer ,  int


# isinstance() - return True or False
value = 99
print(isinstance(value, int))

print(isinstance(value, float))


# test boolean literal
value = True
print(value, type(value))
print(isinstance(value, bool))
print(isinstance(value, int))

print(value + 1)
print()

# type()  get the datatype of a literal or variable (constant)
# isinstance(v, type)


# data types
"""
int
float
bool
str
"""


# GROUP1. Numbers
# case 1. int
h1 = 0x10
print(h1, type(h1))

# case 2. float
f1 = 1.23
print(f1, type(f1))

# case 3. complex
c1 = 1 + 3j
print(c1, type(c1))

# GROUP2. Strings
s1 = 'abc'
print(s1, type(s1))

# GROUP3. Boolean
b1 = True
print(b1, type(b1))
b2 = False
print(b2, type(b2))

# GROUP4. Collection

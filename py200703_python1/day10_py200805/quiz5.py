"""
quiz 5
"""


# q1.
bool1 = True
print(type(bool1))

print(isinstance(bool1, int))

# q2.
#int
print(type(123))

# float
# complex
print(type(1+4j))

# q3
b1 = 0b10
o1 = 0o10
x1 = 0x10

f1 = 1.23e2
f2 = 1.23e-2

# q4
n1 = 2
print(n1, type(n1))
# type(n1)

# q5.
num = 9
print(isinstance(num, int))
print()

# q6.
# quiz5_yourname.py
# define, declare, create, new
# 6.2
mylist = [1,2,3,4,5,6]
print(mylist[0])
print(mylist[len(mylist)-1])
print(mylist[-1])
print(mylist[5])

# 6.3
mylist[3] = 999
print(mylist)

# 6.4
mytuple = (1,2,3,4,5,6)
print(mytuple)
print(mytuple[0])
print(mytuple[-1])
# a = 10
# a = 20

# 6.5
# mytuple[3] = 999

# 6.6
myset={1,1,2,2,3,3}
print(myset)

# 6.7
dict1 = {
    'k1' : 'v1',
    'k2' : 'v2'
}
print(dict1)

# 7.
# float -> str
# str()

# str -> int
# int('xxx')


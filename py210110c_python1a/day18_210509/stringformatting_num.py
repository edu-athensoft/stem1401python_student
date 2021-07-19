"""
Number Formatting Types
Type	Meaning
d	Decimal integer
c	Corresponding Unicode character
b	Binary format

o	Octal format
x	Hexadecimal format (lower case)
X	Hexadecimal format (upper case)

n	Same as 'd'. Except it uses current locale setting for number separator
e	Exponential notation. (lowercase e)
E	Exponential notation (uppercase E)

f	Displays fixed point number (Default: 6)
F	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'

g	General format. Rounds number to p significant digits. (Default precision: 6)
G	Same as 'g'. Except switches to 'E' if the number is large.

%	Percentage. Multiples by 100 and puts % at the end.

"""

# case 1.
num = 10.1
# str1 = 'I am testing the data: {:5d}'.format(num)
# ValueError: Unknown format code 'd' for object of type 'float'

num = 10
# str1 = 'I am testing the data: {:5.0d}'.format(num)
# ValueError: Precision not allowed in integer format specifier

str1 = 'I am testing the data: {:5d}'.format(num)
print(str1)


# case 2.
# c	Corresponding Unicode character
char = 200
str2 = 'I am testing the data: {:c}'.format(char)
print(str2)

char = 201
str2 = 'I am testing the data: {:c}'.format(char)
print(str2)

char = 202
str2 = 'I am testing the data: {:c}'.format(char)
print(str2)


# case 3.
num = 200
str3 = 'I am testing the data: {:b}'.format(num)
print(str3)

print(0b11001000)


# g
num = 1.23456789
str4 = 'I am testing the data: {:g}'.format(num)
print(num)


# o, x,  X
# Leonj
num = 200
str2 ='i am testing the data: {:o}'.format(num)
print(str2)

num = 200
str2 ='i am testing the data: {:x}'.format(num)
print(str2)

num = 200
str2 ='i am testing the data: {:X}'.format(num)
print(str2)

# Andy
# case 4.
num3 = 200
str2 = "I am testing the data: {:o}".format(num3)
print(str2)
print(0o310)

# case 5.
num4 = 200
str2 = "I am testing the data: {:x}".format(num4)
print(str2)
print(0xc8)

# case 6.
num5 = 200
str2 = "I am testing the data: {:X}".format(num5)
print(str2)
print(0xC8)


# Yiding
num = 200
str2 ='testing the data: {:X}'.format(num)
print(str2)

num = 200
str2 ='testing the data: {:o}'.format(num)
print(str2)

num = 200
str2 ='testing the data: {:x}'.format(num)
print(str2)

print(hex(200))
print(oct(200))

# Leonj
num = 200.12356789
str2 ='i am testing the data: {:g}'.format(num)
print(str2)

num = 200.12856789
str2 ='i am testing the data: {:.5g}'.format(num)
print(str2)

num = 200.123456789
str2 ='i am testing the data: {:G}'.format(num)
print(str2)








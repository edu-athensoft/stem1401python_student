"""
[Homework]
Write codes to try out number formatting type
Date: 2021-05-09
Due date: by the end of next Sat.
"""
# case 1
num1 = 10

str1 = "I am testing the data: {:5d}".format(num1)
print(str1)
print('======')

# case 2.
char = 200
str2 = "I am testing the data: {:c}".format(char)
print(str2)

char = 201
str2 = "I am testing the data: {:c}".format(char)
print(str2)

char = 202
str2 = "I am testing the data: {:c}".format(char)
print(str2)
print('======')

# case 3.
num2 = 200
str2 = "I am testing the data: {:b}".format(num2)
print(str2)
print(0b11001000)
print('======')

# case 4.
num3 = 200
str2 = "I am testing the data: {:o}".format(num3)
print(str2)
print(0o310)
print('======')

# case 5.
num4 = 200
str2 = "I am testing the data: {:x}".format(num4)
print(str2)
print(0xc8)
print('======')

# case 6.
num5 = 200
str2 = "I am testing the data: {:X}".format(num5)
print(str2)
print(0xC8)
print('======')

# case 7.
num5 = 200
str2 = "I am testing the data: {:n}".format(num5)
print(str2)
print('======')

# case 8.
num5 = 200
str2 = "I am testing the data: {:e}".format(num5)
print(str2)
print(2.000000e+02)
print('======')

# case 9.
num5 = 200
str2 = "I am testing the data: {:E}".format(num5)
print(str2)
print(2.000000E+02)
print('======')

# case 10.
num5 = 200
str2 = "I am testing the data: {:f}".format(num5)
print(str2)
print('======')

# case 11.
num5 = 200
str2 = "I am testing the data: {:F}".format(num5)
print(str2)
print('======')

# case 12.
num5 = 1.23456789
str2 = "I am testing the data: {:g}".format(num5)
print(str2)
print('======')

# case 13
str2 = "I am testing the data: {:G}".format(num5)
print(str2)
print('======')

# case 14
num5 = 200
str2 = "I am testing the data: {:%}".format(num5)
print(str2)

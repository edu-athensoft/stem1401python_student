"""
[Homework] Yiding

"""

num1 = 10

str1 = "I am testing the data: {:5d}".format(num1)
print(str1)
print('======')


char = 300
str2 = "I am testing the data: {:c}".format(char)
print(str2)

char = 301
str2 = "I am testing the data: {:c}".format(char)
print(str2)

char = 302
str2 = "I am testing the data: {:c}".format(char)
print(str2)
print('======')


num2 = 300
str2 = "I am testing the data: {:b}".format(num2)
print(str2)
print(0b11001000)
print('======')


num3 = 300
str2 = "I am testing the data: {:o}".format(num3)
print(str2)
print(0o310)
print('======')


num4 = 300
str2 = "I am testing the data: {:x}".format(num4)
print(str2)
print(0xc8)
print('======')


num5 = 300
str2 = "I am testing the data: {:X}".format(num5)
print(str2)
print(0xC8)
print('======')


num5 = 300
str2 = "I am testing the data: {:n}".format(num5)
print(str2)
print('======')


num5 = 300
str2 = "I am testing the data: {:e}".format(num5)
print(str2)
print(2.000000e+02)
print('======')


num5 = 300
str2 = "I am testing the data: {:E}".format(num5)
print(str2)
print(2.000000E+02)
print('======')


num5 = 300
str2 = "I am testing the data: {:f}".format(num5)
print(str2)
print('======')


num5 = 300
str2 = "I am testing the data: {:F}".format(num5)
print(str2)
print('======')


num5 = 1.23456
str2 = "I am testing the data: {:g}".format(num5)
print(str2)
print('======')


str2 = "I am testing the data: {:G}".format(num5)
print(str2)
print('======')

num5 = 300
str2 = "I am testing the data: {:%}".format(num5)
print(str2)
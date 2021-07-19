"""
leon
homework
write codes to try out number formatting type
Due date by the end of next saturday
"""

num = 10

str1 = 'I am testing the data: {:5d}'.format(num)
print(str1)

char = 200
str2 = 'I am testing the data: {:c}'.format(char)
print(str2)

char = 201
str2 = 'I am testing the data: {:b}'.format(char)
print(str2)

char = 201
str2 = 'I am testing the data: {:o}'.format(char)
print(str2)

char = 201
str2 = 'I am testing the data: {:x}'.format(char)
print(str2)

char = 201
str2 = 'I am testing the data: {:X}'.format(char)
print(str2)

char = 201.102
str2 = 'I am testing the data: {:n}'.format(char)
print(str2)

char = 201
str2 = 'I am testing the data: {:e}'.format(char)
print(str2)

char = 201
str2 = 'I am testing the data: {:E}'.format(char)
print(str2)

char = 201
str2 = 'I am testing the data: {:f}'.format(char)
print(str2)
char = 201
str2 = 'I am testing the data: {:F}'.format(char)
print(str2)

num = 200.1234
str2 ='i am testing the data: {:.5g}'.format(num)
print(str2)

num = 200.1234
str2 ='i am testing the data: {:G}'.format(num)
print(str2)




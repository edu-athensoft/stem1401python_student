"""
datatype conversion
"""

print(12,34)
print('12','34')

print(12+34)
print('12'+'34')

# how to perform datatype conversion
# to change the datatype of a value/variable

# string -> number (int, float)
n1 = '123'
n2 = '234'
result = float(n1) + float(n2)
print("Result 1 =",result)

n1 = '123'
n2 = '234'
result = int(n1) + int(n2)
print("Result 2 =",result)

n3 = '123.0'       # incompatible literal
# result = int(n3)
# print("Result 3 =",result)

n4 = 123.1
result = int(n4)
print("Result 4 =",result)
print()

# string -> float
f1 = '123.1'
result = float(f1)
print("Result f1 =",result)

f2 = '123'
result = float(f2)
print("Result f2 =",result)

f3 = '1.23e2'
result = float(f3)
print("Result f3 =",result)

f4 = 'abc'
# result = float(f4)
# print("Result f4 =",result)
print()

# number -> string
num = 5.67
print(num,type(num))
x = str(num)
print(x, type(x))






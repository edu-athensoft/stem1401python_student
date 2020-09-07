"""
ex 2.
write a program to find the smallest number among 3 given numbers
"""

a = 24
b = 15
c = 6
d = 78

max = a

# 1st round
if max < a:
    max = a

# 2nd round
if max < b:
    max = b

# 3rd round
if max < c:
    max = c

# 4th round
if max < d:
    max = d

print("The max number is {}".format(max))



#
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

min = num1

if num1<min:
    min = num1
if num2<min:
    min = num2
if num3<min:
    min = num3

print("The smallest number is {}".format(min))

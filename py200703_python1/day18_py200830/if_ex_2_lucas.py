"""
ex 2.
write a program to find the largest number among 3 given numbers
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1>num2 and num1>num3:
    largest_num = num1
elif num2>num1 and num2>num3:
    largest_num = num2
else:
    largest_num = num3

print("The largest number is {}".format(largest_num))


#
"""
case 1.
num1>num2 and num1>num3
=> num1 -> max

case 2.
num2>num1 and num2>num3
=> num2 -> max

case 2.
num3>num1 and num3>num2
=> num3 -> max

"""
# largest_num = None
#
# if num1>num2 and num1>num3:
#     largest_num = num1
#
# if num2>num1 and num2>num3:
#     largest_num = num2
#
# if num3>num1 and num3>num2:
#     largest_num = num3
#
# print("The largest number is {}".format(largest_num))
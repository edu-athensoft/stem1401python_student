
"""
[Homework]
1. Rewriting arithmetic calculator.
Accepting 2 inputs from a keyboard by users and output the division of these 2 values.
Requirements:
The 2 inputs should be converted to Integer before calculating.
Exception handling is required.
Your program should never crash in any case of input.
You may optimize your program.

"""
print("Welcome To My Mini Calculator")
num1 = input("Please input one number to be the dividend: ")
num2 = input("Please input one number to be the divisor: ")

try:
    num1 = int(num1)
except Exception as except_probl:
    print("This number {} is wrong, please try again.".format(num1))
    print(except_probl)

try:
    num2 = int(num2)
except Exception as except_probl2:
    print("This number {} is wrong, please try again.".format(num1))
    print(except_probl2)


try:
    res = num1 / num2
    print("result: ", res)
except Exception as except_probleme2:
    print(except_probleme2)

print("====== End =======")




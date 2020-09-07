"""
if-statement

nested if-statement
"""

# to test if a given number is a positive , zero, or negative number
# output the message

#
# num = 0
num = float(input("Enter a number:"))
# print(type(num))

# num = float(num)

if num >= 0:
    if num > 0:
        print("positive")
    else:
        print("zero")
else:
    print("negative")

# 3 tests passed
# then write input()





"""
multiplication table 1

Python Program to Display the multiplication Table
Required:
Python for Loop
Python Input, Output and Import

input from keyboard:  10

Sample Result:
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120

input from keyboard:  8

12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96

input from keyboard:  N
12 x 1 = 12
12 x 2 = 12
....
12 x N = 12*N
"""


# input
# num = input("Enter a number (num > 0):")
# num = int(num)
num = int(input("Enter a number (num > 0):"))
# print(type(num), num)

# print out table
# range(1, STOP)
A = 10

STOP = num + 1
for i in range(1,STOP):
    # print(i)
    result = A * 1
    print("{} x {} = {}".format(A, i, result))


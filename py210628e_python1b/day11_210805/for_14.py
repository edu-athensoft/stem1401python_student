"""
multiplication table 1

Python Program to Display the multiplication Table
Required:
Python for Loop
Python Input, Output and Import

Sample Result:
input from keyboard:  N
N x 1 = N
N x 2 = N
....
N x N = N*N
"""


# input
num = int(input("Enter a number (num > 0):"))

# print out table
A = num

STOP = num + 1
for i in range(1,STOP):
    result = A * 1
    print("{} x {} = {}".format(A, i, result))


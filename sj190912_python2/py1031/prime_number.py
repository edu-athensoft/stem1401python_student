"""
tell if a given number n is a prime number
if n is a prime number
    print out : Yes, the number of {} is a prime number
else
    print out : No, it is not a prime number
"""

# n = 11
#
# 1,2,3,4,5,6,...,11   (n times)
# i = 2 .. (n-1)
#
# 11 % i == 0
#   not a prime number


# input a number
number = int(input("Enter a positive integer:"))

if number > 1:
# test if number is a prime number
# [2,3,4,5,6,7,8,...,number-1]
    for i in range(2, number):
        if number % i == 0:
            print("No, the number is not a prime number".format(number))
            print("{} can be divided by {} and {}".format(number,i, number//i))
            break
    else:
        print("Yes, the number of {} is a prime number".format(number))
else:
    print("Not a valid number")





















# n = 59
# n = 113
#
# number = int(input("Enter an integer:"))
#
# a = 1
# print(type(a))
# print(isinstance(a, int) )
#
# # even number
# # a % 2 == 0
#
#
# for i in [1,2,3,4,5,6,7,8]:
#     if i == 7:
#         break;


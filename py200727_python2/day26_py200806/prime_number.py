"""
Write a program to check if a given number is a Prime number

Prime number:
(not composite number)
"""

# kevin
# num = 7
#
# #
# a = ""
#
# for i in range(1,num):
#     if num % i != 0:
#         a = False
#     else:
#         a = True
#
# if a:
#     print("{} is a prime number.".format(num))
# else:
#     print("{} is not a prime number.".format(num))


# qi jun
num = 11
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("{} is not a prime number".format(num))
            print(i, "times", num/i , "is", num)
            break
        else:
            print("{} is a prime number".format(num))

else:
    print("{} is a prime number".format(num))



"""
Write a program to check if a given number is a Prime number

Prime number:
(not composite number)

"""

num = 107

"""
hints:
for loop or while loop
break and continue
if-statement
"""

if num > 1:
    # check for factors
    for i in range(2, num):
        if num % i == 0:
            print("{} is not a prime number".format(num))
            print(i, "times", num/i , "is", num)
            break
        else:
            print("{} is a prime number".format(num))

else:
    print("{} is a prime number".format(num))





"""
Homework 3
"""

# Question 5 find the factorial of a number

num_1 = int(input(""))


def factorial_calculator(x):
    factorial_amount = 1
    for i in range(1, x + 1):
        factorial_amount *= i
    return factorial_amount


print(factorial_calculator(num_1))


# Question 6 prove that a number is between a given range

num_2 = int(input(""))


def range_motion(y):
    if 10 < y < 30:
        print("{} is between 10 and 30".format(y))
    else:
        print("{} is not between 10 and 30".format(y))


range_motion(num_2)


# Question 7 find the number of lower and upper case letters in a string

str_1 = input("")


def find_lower_and_upper(z):
    lower_count = 0
    upper_count = 0
    for i in list(z):
        if str(i) == str(i).lower():
            lower_count += 1
        elif str(i) == str(i).upper():
            upper_count += 1
    return lower_count, upper_count


print("There are {} lowercase letters and {} uppercase letters".format(find_lower_and_upper(str_1)[0], find_lower_and_upper(str_1)[1]))
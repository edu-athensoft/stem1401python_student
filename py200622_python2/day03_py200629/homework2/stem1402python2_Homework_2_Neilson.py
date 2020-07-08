"""
Homework 2
Neilson Tao
"""


# Question 1 Find the Max of 3 numbers


def Finder_biggest_num(a, b, c):
    biggest_num = a
    list_1 = [a, b, c]
    for i in list_1:
        if biggest_num < i:
            biggest_num = i
    return biggest_num


print("The biggest num is {}".format(Finder_biggest_num(3, 2, 4)))


# Question 2 add up all the numbers in a list


list_2 = [4, 2, 6, 1, 2, 5, 7]


def sum_of_list(x):
    final_sum = 0
    for i in list_2:
        final_sum += i
    return final_sum


print("The sum of the numbers in the list is {}".format(sum_of_list(list_2)))

# Question 3 multiply all the numbers in a list


def product_or_list(y):
    final_product = 1
    for i in list_2:
        final_product *= i
    return final_product


print("The product of the numbers in the list is {}".format(product_or_list(list_2)))

# Question 4 Reverse a string

str_1 = "hello"


def reverse(z):
    final_string = ""
    list_str_1 = list(str_1)
    list_str_1.reverse()
    for i in list_str_1:
        final_string += i
    return final_string


print("The string hello reversed is {}".format(reverse(str_1)))

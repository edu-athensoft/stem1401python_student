"""
For June 29th, 2020
Ken
stem1402_python_homework_2_ken
"""

# Question 1

def max_of_three_numbers(n1, n2, n3):
    """
    finding the biggest of three numbers
    :param n1: first number
    :param n2: second number
    :param n3: third number
    :return: biggest number
    """
    biggest_number = n1
    if n2 > biggest_number:
        biggest_number = n2
    if n3 > biggest_number:
        biggest_number = n3
    return biggest_number


# Question 2

def sum_of_numbers_list(list):
    """
    Sums the numbers in the list.
    :param list: list of numbers
    :return: sum of all the numbers in the list
    """
    sum = 0
    for number in list:
        sum += number
    return sum


# Question 3

def product_of_numbers_list(list):
    """
    Multiplies the numbers in the list.
    :param list: list of numbers
    :return: Product of all the numbers in the list
    """
    product = 1
    for number in list:
        product *= number
    return product


# Question 4

def string_reverser(string):
    list_of_string = list(string)
    list_of_string.reverse()
    reversed_string = "".join(list_of_string)
    return reversed_string




# Testing

print("1. Max number out of 3")

a = 3
b = 15
c = -23

print("The biggest number out of {}, {} and {} is {}.".format(a,b,c,max_of_three_numbers(a,b,c)))


print("2. Sum of numbers in a list")

list1 = [2,3,5,2,1]

print("The sum of the numbers of the list is {}.".format(sum_of_numbers_list(list1)))


print("3. Product of numbers in a list")

print("The product of the numbers of the list is {}.".format(product_of_numbers_list(list1)))


print("4. String reverser")

string1 = "fedcba"

print('The reverse of "{}" is "{}".'.format(string1, string_reverser(string1)))
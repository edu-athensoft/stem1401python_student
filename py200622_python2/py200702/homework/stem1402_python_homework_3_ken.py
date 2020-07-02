"""
For July 2nd, 2020.
stem1402_python_homework_3_ken
Ken
"""


# 1. Write a Python function to find the Max of three numbers.
def find_max_of_numbers(*numbers):
    """
    Finds max number with for loop and condition.
    :param numbers: numbers from which the biggest will be picked out
    :return: max number
    """
    max_number = numbers[0]
    for current_number in numbers:
        if max_number < current_number:
            max_number = current_number
    return  max_number


# test
print("Function 1: Max number.", find_max_of_numbers(5,1,2,100,-58))


# 2. Write a Python function to sum all the numbers in a list.
def find_sum_of_numbers(list1):
    """
    Finds sum
    :param list1: list from which numbers will be added
    :return: sum of the numbers
    """
    sum = 0
    for current_number in list1:
        sum += current_number
    return sum


# test
print("Function 2: Sum of numbers.", find_sum_of_numbers([3,2,5,1,2]))


# 3. Write a Python function to multiply all the numbers in a list.
def find_product_of_numbers(list1):
    """
    Finds product
    :param list1: list from which numbers will be multiplied
    :return: product
    """
    product = 1
    for current_number in list1:
        product += current_number
    return product


# test
print("Function 3: Product of numbers.", find_product_of_numbers([-192,2,1,4]))


# 4. Write a Python program to reverse a string
def string_reverser(string):
    """
    string is reversed by concatenating the letters of the original string in backwards order to a new string
    :param string: string that'll be reversed
    :return: reversed string
    """
    reversed_string = ""
    for index in range(len(string)-1, -1, -1):
        reversed_string += string[index]
    return reversed_string

# test
print("Function 4: String reverser.", string_reverser("abcdefg"))


# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial_finder(number):
    """
    will multiply all numbers from 1 to the numbers, factorial
    :param number: number from which the factorial will be calculated
    :return: factorial
    """
    factorial = 1
    for current_number in range(2, number + 1):
        factorial *= current_number
    return factorial

# test
print("Function 5: Factorial finder.", factorial_finder(12))


# 6. Write a Python function to check whether a number is in a given range.
def range_checker(number, bottom_limit_inclusive, upper_limit_inclusive):
    """

    :param number: number whose inclusiveness will be checked
    :param bottom_limit_inclusive: lowest number in the range
    :param upper_limit_inclusive: highest number in the range
    :return: boolean of the condition whether or not the number is within the range
    """
    inside = False
    if bottom_limit_inclusive <= number <= upper_limit_inclusive:
        inside = True
    return inside

# test
print("Function 6: Range checker.", range_checker(5772, -321, 420))


# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def case_counter(string):
    """
    using for loop, will check every character and add to a sum if it's capital or if it's lowercase
    :param string: string that'll be checked
    :return: tuple, first value is the number of uppercase letters, second value is the number of lowercase letters
    """
    upper = 0
    lower= 0
    for current_letter in string:
        if current_letter in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            upper += 1
        if current_letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            lower += 1
    return upper, lower

# test
print("Function 7: Case counter.", case_counter("fhadhfdHHAIHhfhdaHIH"))



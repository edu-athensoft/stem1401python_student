"""
exception handling

raise an error
"""

# input a positive number, otherwise we raise an error

try:
    a = int(input("Enter a positive integer:"))
    if a <= 0:
        raise ValueError("That is not a positive number ")
# except Exception as e:
#     print(e)
except ValueError as ve:
    print(ve)


# test 1. input a string
# invalid literal for int() with base 10: 'uasdfjasdf'

# test 2. input a floating number
# invalid literal for int() with base 10: '1.5'

# test 3. -8
# NO ERROR!



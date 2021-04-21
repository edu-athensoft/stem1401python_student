"""
raise an error

throw
throws
raise

keyword: raise

1. we can raise an error as we want to (when, where and what)
2. we can add a message when raising an error

logical error / exception
"""

# input a positive integer


try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("Value should be a positive integer!")
except ValueError as ve:
    print(ve)





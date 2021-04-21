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

# Rules
# input a positive integer
# positive integer should be in the range of 1 to 100



try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("Value should be a positive integer!")

    if num > 100:
        raise ValueError("Too big!")
except ValueError as ve:
    print(ve)





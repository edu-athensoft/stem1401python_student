"""
docstring in functions
"""

# docstring in function without argument
def foo():
    """
    the description of this function
    :return:
    """
    print("Yes, we entered the function of foo()")

# call a function
foo()
print("Good bye!")


# docstring in function with arguments
def add(num1, num2):
    """
    the description of this function add()
    :param num1:
    :param num2:
    :return:
    """
    res = num1 + num2
    return res

result = add(3, 5)

print(foo.__doc__)
print(add.__doc__)
"""
user-defined exception

1. what is ude?

2. benefits

3. how to use?
step1. create/define exception
step2. use exception

"""

"""
keyword:  class
"""


class CustomError(Exception):
    pass

class TooBigError(Exception):
    pass

class TooSmallError(Exception):
    pass


# test
# raise CustomError("This is a custom error")

try:
    print(f"Let's try out user defined error!")
    print("Enter a number:")
    num = float(input())
    if num > 100:
        raise TooBigError("Too Big")
    elif num < 1:
        raise TooSmallError("Too Small")
    else:
        raise CustomError("This is a custom error")
except CustomError as ce:
    print(ce)
except TooBigError as be:
    print(be)
except TooSmallError as se:
    print(se)
finally:
    print("done.")


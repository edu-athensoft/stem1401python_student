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


# test
raise CustomError("This is a custom error")


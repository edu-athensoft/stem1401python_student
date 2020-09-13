"""
module : exception handling
creating Custom Exceptions

"""


# define a user-defined error
class CustomError(Exception):
    pass


class CustomError2(Exception):
    pass


# to use the error
raise CustomError

raise CustomError2

# to change the order of raise statements



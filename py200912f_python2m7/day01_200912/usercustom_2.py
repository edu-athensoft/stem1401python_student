"""
module : exception handling
creating Custom Exceptions

"""


# define a user-defined error
class CustomError(Exception):
    pass


# to use the error
raise CustomError("This is a cust error")




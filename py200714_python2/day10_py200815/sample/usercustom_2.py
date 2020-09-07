"""
module : exception handling
creating Custom Exceptions with description

"""


class CustomError(Exception):
    pass


raise CustomError("An CustomError occurred")


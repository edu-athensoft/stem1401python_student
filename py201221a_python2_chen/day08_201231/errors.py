"""
definitions of errors(exceptions)
best practice
"""

class CustomError(Exception):
    pass


class Custom2Error(Exception):
    pass


class Custom3Error(Exception):
    pass


class Error(Exception):
    pass


class ValueTooLargeError(Error):
    pass


class ValueTooSmallError(Error):
    pass


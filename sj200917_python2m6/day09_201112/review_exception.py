"""
User-defined Exceptions

1. what is it?
2. how to write
3. how to use
4. why to use
    a. Built-in error
    b. ValueError,  ValueError
    c. reusable

Exception/Error
    Runtime
    Logical

Built-in Error
    20-30

Syntax

try:
    pass
except:
    pass
except:
    pass
else:
    pass
finally:
    pass


try:
    pass
except:
    pass


try:
    pass
except:
    pass
else:
    pass

try:
    pass
finally:
    pass


catch specific error
except SpecificErrorName
except (ErrorName1, ErrorName2, ...)

exception/error category
    Concrete error type
    Exception


"""

class CustomError(Exception):
    pass



condition = True

if condition:
    raise CustomError("This is a customError")


"""
import external error classes

errors.py
exceptions.py
error.y
exception.py
"""
class CustomError(Exception):
    pass

class CustomError2(Exception):
    pass

class CustomError3(Exception):
    pass


try:
    raise CustomError3("An error3 occurred")
    raise CustomError2("An error2 occurred")
    raise CustomError("An error1 occurred")

except CustomError as e1:
    print(e1)

except CustomError2 as e2:
    print(e2)

except CustomError3 as e3:
    print(e3)

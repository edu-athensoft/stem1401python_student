"""
import external error classes

errors.py
exceptions.py
error.y
exception.py
"""

import py200510_python2.day17_py200712.errors as err

try:
    raise err.CustomError3("An error3 occurred")
    raise err.CustomError2("An error2 occurred")
    raise err.CustomError("An error1 occurred")

except err.CustomError as e1:
    print(e1)

except err.CustomError2 as e2:
    print(e2)

except err.CustomError3 as e3:
    print(e3)

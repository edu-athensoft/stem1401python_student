"""
import module of errors

"""

import py200912f_python2.day01_200912.errors as err

print("start")

try:
    num = input("Enter a number:")

    if num == '1':
        raise err.UserError1("err1")

    if num == '2':
        raise err.UserError2("err2")

    if num == '3':
        raise err.UserError3("err3")

except err.UserError1 as e1:
    print(e1)

except err.UserError2 as e2:
    print(e2)

except err.UserError3 as e3:
    print(e3)

print("bye")


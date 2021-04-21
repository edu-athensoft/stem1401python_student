"""
main module owned by you

how to use errors defined in errors.py

hint:

import

compose some codes to raise errors

"""

import py201221a_python2_chen.day08_201231.errors as err


try:

    num = input("Enter the no. of Custom Error Type [1,2,3]: ")

    if num == '1':
        raise err.CustomError("this is message of CustomError")

    elif num == '2':
        raise err.Custom2Error("this is message of CustomError2")

    elif num == '3':
        raise err.Custom3Error("this is message of CustomError3")

    else:
        print("No errors!")

except err.CustomError as ce:
    print(ce)

except err.Custom2Error as ce:
    print(ce)

except err.Custom3Error as ce:
    print(ce)

finally:
    print("Test of Custom Errors done.")











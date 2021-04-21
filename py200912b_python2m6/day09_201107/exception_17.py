"""
User-defined Error

keyword:  class

step1. define

step2. use
"""

# import py200912b_python2m6.day09_201107.myerrors as err

from py200912b_python2m6.day09_201107.myerrors import *

try:
    print("Enter a number between 20 and 30: ", end="")
    num = int(input())

    if num < 20:
        raise TooSmallNumberError("Number is too small.")

    if num > 30:
        raise TooBigNumberError("Number is too big.")

except TooSmallNumberError as ue1:
    print(ue1)

except TooBigNumberError as ue2:
    print(ue2)

except Exception as e:
    print(e)

finally:
    print("done.")


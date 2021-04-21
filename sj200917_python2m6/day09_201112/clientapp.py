"""
Test user-defined errors
"""


# user input a number from a keyboard
# if it is > 100, then raise an error
# if it is < 1, then raise an error also

import sj200917_python2m6.day09_201112.myerrors as err

print("Please enter a number from 1 to 100: ", end="")
num = int(input())


try:
    if num> 100:
        raise err.TooBigError

    elif num < 1:
        raise err.TooSmallError

except err.TooBigError as tbe:
    print("Too big! please input a number which is less than 100.")

except err.TooSmallError as tse:
    print("Too small! please input a number which is greater than 1.")

except Exception as e:
    print(e)

print("continue to execute.")

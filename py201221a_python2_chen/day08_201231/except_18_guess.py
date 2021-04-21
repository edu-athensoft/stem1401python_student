"""
guessing number game

"""

import py201221a_python2_chen.day08_201231.errors as err

# the target number
number = 10


while True:
    try:
        i_num = int(input("Enter a nubmer: "))
        if i_num < number:
            raise err.ValueTooSmallError("Too small")
        elif i_num > number:
            raise err.ValueTooLargeError("Too large")
        break

    except err.ValueTooSmallError as vse:
        print("This value you input is too small!")
        print()

    except err.ValueTooLargeError as vle:
        print("This value you input is too large!")
        print()

    except ValueError as ve:
        print("Please input a valid number!")
        print()


print("Congratulations!")

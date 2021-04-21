"""
Test user-defined errors

input until accepted or valid
"""


# user input a number from a keyboard
# if it is > 100, then raise an error
# if it is < 1, then raise an error also
# if user input whitespace (aka empty input), then raise EmptyInputError


import sj200917_python2m6.day09_201112.myerrors3 as err


while True:
    try:
        print("Please enter a number from 1 to 100: ", end="")
        raw_input = input()

        if raw_input.isspace() or len(raw_input)==0:
            raise err.EmptyInputError

        num = float(raw_input)

        if num > 100:
            raise err.TooBigError

        elif num < 1:
            raise err.TooSmallError

    except err.EmptyInputError as tbe:
        print("Empty input, please try again!")

    except err.TooBigError as tbe:
        print("Too big! please input a number which is less than 100.")

    except err.TooSmallError as tse:
        print("Too small! please input a number which is greater than 1.")

    except Exception as e:
        print("Invalid input, please try again!")
        # print(e)
    else:
        break

    print()

print(f"You've input {num}.")

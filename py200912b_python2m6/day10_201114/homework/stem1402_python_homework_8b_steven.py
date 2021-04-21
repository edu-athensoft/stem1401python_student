"""
stem1402_python_homework_8b_steven
"""

import random

# import user-defined errors from stem1402_python_homework_8b_errors
from py200912b_python2m6.day10_201114.homework.stem1402_python_homework_8b_errors import TooSmallNumberError, TooBigNumberError

# num1 is the answer
num1 = random.randint(1, 101)

limit1 = 1
limit2 = 100
counter = 1


print("Number Guessing Game")
print("=== START ===")
print("You got 8 chances")

# flag of while loop
y = True

while y:
    try:
        while counter <= 8:
            print()
            x = int(input(f"Enter a number from {limit1} to {limit2}:"))

            # if the number is too small
            if x < num1:
                if x > limit1:
                        print(f"{x} is too small")
                        limit1 = x
                        counter += 1
                # if the number is out of range
                # every time the number is out of range, the counter won't go up


            # if the number is too big
            if x > num1 :
                if x < limit2:
                        print(f"{x} is too big")
                        limit2 = x
                        counter += 1
                # if the number is out of range
                # every time the number is out of range, the counter won't go up


            # if you guess the right number
            if x == num1:
                    print()
                    print(f"You won! {x} is the right number")
                    print("Goodbye")
                    print("=== END ===")
                    y = False
                    break

            # if you didn't guess correctly after 8 tries
            if counter == 9:
                    print()
                    print("Sorry you lost")
                    print("You didn't guess the right number")
                    print("Goodbye")
                    print("=== END ===")
                    y = False
                    break

            # out of range answers don't make the counter go up
            if x < limit1:
                print("Number out of range")
                raise TooSmallNumberError(f"Number should not be less than {limit1}.")

            if x > limit2:
                print("Number out of range")
                raise TooBigNumberError(f"Number should not be greater than {limit2}.")


    except TooSmallNumberError as ue1:
        print(ue1)
    except TooBigNumberError as ue2:
        print(ue2)
    except ValueError:
            print("Try to input a valid literal that can transform to an integer (item with base 10)")
    except Exception:
            print("Unknown Error")
            print("Please try again")

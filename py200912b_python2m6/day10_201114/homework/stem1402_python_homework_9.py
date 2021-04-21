"""
Homework 9
"""

import random
from py201107.errors import *

randint = random.randint(1, 100)
guess = 0

print("Guess a number between 1 and 100")
for i in range(8):
    guess += 1

    valid = False
    while not valid:
        try:
            print()
            num = int(input("Please enter a number: "))

        except ValueError:
            print("Invalid characters. Please try again.")
            
        else:
            try:
                if num < 1:
                    raise NumberTooSmallError("The number is not in the given range. It should be smaller.")

                elif num > 100:
                    raise NumberTooBigError("The number is not in the given range. It should be bigger.")

            except NumberTooBigError as ntb:
                print(ntb)

            except NumberTooSmallError as nts:
                print(nts)

            else:
                valid = True

    if num == randint:
        print("Congratulations! You found the right number.")
        break

    elif guess == 8:
        pass

    else:
        if num < randint:
            print("That is not the right number. Please try again. The number is higher.")

        else:
            print("That is not the right number. Please try again. The number is lower.")

print()
if num != randint:
    print(f"Sorry, that was your last chance! The number was {randint}")

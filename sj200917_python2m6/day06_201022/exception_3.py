"""
exception handling for user input
"""

import sys


while True:
    try:
        number = int(input("Enter a number: "))
        print(number)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Input again please!")
        print()




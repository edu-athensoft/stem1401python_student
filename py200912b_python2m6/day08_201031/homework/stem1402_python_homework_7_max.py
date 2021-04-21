"""
Homework 7
"""

print("Welcome to the arithmetic calculator!")

valid = False
while not valid:
    try:
        print()
        num_1 = int(input("Please enter your first number: "))
    except ValueError:
        print("Invalid characters. Please try again.")
    except Exception:
        print("Unknown error.")
    else:
        valid = True

valid = False
while not valid:
    try:
        print()
        num_2 = int(input("Please enter your second number: "))
    except ValueError as ve:
        print("Error: 33001. Invalid characters. Please try again.")
        # print(ve)
    except Exception as e:
        print("Unknown error.")
        print(e)
    else:
        valid = True

print()


try:
    print(f"The answer is {num_1 / num_2}")
except ZeroDivisionError:
    print("0 is not valid for division.")
except Exception:
    print("Unknown error.")

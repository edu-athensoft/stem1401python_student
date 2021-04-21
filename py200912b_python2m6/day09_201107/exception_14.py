"""
user-defined exception

case 1. 100
case 2. 1
case 3. 0
case 4. 101

"""


try:
    print("Enter a number between 1 and 100: ", end="")
    num = int(input())

    if num < 1:
        raise ValueError

    if num > 100:
        raise ValueError

except ValueError as ve:
    print("Value Error!")
    print(ve)

except Exception as e:
    print(e)

finally:
    print("done.")

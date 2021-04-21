"""
stem1402_python_homework_7_steven
"""

def divide(x,y):
    return x / y

print("This is a calculator with only the divide operation")
print("=== start ===")
while True:

    try:
        x = int(input("Please enter the first number:"))
        y = int(input("Please enter the second number:"))
        print()
        print(f"{x} / {y} =", divide(x,y))
        print()
        a = input("Do you wish to quit? Please enter 'Yes' or 'No':")
        a = a.lower()
        if a in ("no", "n"):
            print()
            print("----------------------------------------------------------------------------------------------")
            continue
        if a in ("yes", 'y'):
            print()
            print("Goodbye")
            print("=== end ===")
            break

    except ValueError:
        print()
        print("ValueError")
        print("Try to input a valid literal that can transform to an integer (item with base 10)")
        print()
        print("----------------------------------------------------------------------------------------------")
    except ZeroDivisionError:
        print()
        print("ZeroDivisionError")
        print("0 is invalid for division")
        print()
        print("----------------------------------------------------------------------------------------------")
    except Exception:
        print()
        print("Unknown Error")
        print("Please check your code!")
        print()
        print("----------------------------------------------------------------------------------------------")

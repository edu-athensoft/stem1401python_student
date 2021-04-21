"""
try...except...finally

try...finally


try:
    pass

except:
    pass
except:
    pass

finally:
    pass
"""


try:
    num = int(input("Enter a number: "))
    # assert num % 2 == 0
    if num %2 != 0:
        raise ValueError;

except AssertionError as ae:
    print("Not an even number")

except ValueError as ve:
    print("Invalid value!")


finally:
    print("Input done.")


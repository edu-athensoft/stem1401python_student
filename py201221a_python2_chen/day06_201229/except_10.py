"""
raising an exception

keyword and syntax:
raise ErrorType("the reason or info in detail")
"""

try:
    # raise KeyboardInterrupt

    number = 20

    if number > 90:
        raise ValueError("Too big.")

    elif number < 30:
        raise ValueError("Too small.")


except KeyboardInterrupt as kbi:
    print(kbi)
    print("there is a keyboardinterrupt event happened")

except ValueError as ve:
    print(ve)









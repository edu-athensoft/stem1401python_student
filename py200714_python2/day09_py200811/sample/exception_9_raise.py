"""
exception handling

raise an error
assert
"""

# input a positive number
# even number (extra)
try:
    a = int(input("Enter a positive integer:"))

    assert a % 2 == 0

    if a <= 0:
        raise ValueError("That is not a positive number ","6666")

except AssertionError:
    print("Not an even number")

except ValueError as ve:
    # print(11111, ve, ve.args[0], ve.args[1])
    print(ve.args[0], ' >>>>> ',ve.args[1])

print("===END===")
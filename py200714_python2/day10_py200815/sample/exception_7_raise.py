"""
exception handling

raise an error
assert
"""

# input a positive number
# even number (extra)

try:
    a = int(input("Enter a positive integer:"))
    if a <= 0:
        raise ValueError("That is not a positive number ")

    assert a % 2 == 0
    assert a <= 100

except ValueError as ve:
    print(ve)

except AssertionError:
    print("Not an even number")
    # print("Not an even number or greater than 100")

print("===END===")
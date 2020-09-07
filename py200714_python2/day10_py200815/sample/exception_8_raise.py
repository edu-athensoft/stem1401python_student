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

    if a % 2 != 0:
        raise ValueError("That is not an even number ")

    if a>100:
        raise ValueError("Greater than 100, too large number")

except ValueError as ve:
    print(ve)

print("===END===")
"""
exception handling
else clause

try:
    pass
finally:
    pass

finally - close resources, release resources
"""

try:
    num = int(input("Enter a integer:"))

    if num <=0:
        raise ValueError("That is not a positive integer")

except ValueError as ve:
    print(ve)

finally:
    print("this is finally clause")

"""
exception handling
else clause

try:
    pass
except:
    pass
else:
    pass

"""

try:
    num = int(input("Enter a integer:"))

    if num <=0:
        raise ValueError("That is not a positive integer")

    assert num % 2 == 0

except ValueError as ve:
    print(ve)

except AssertionError as ae:
    print(ae)
    print("Not a even number")

else:
    reciprocal = 1 / num
    print(reciprocal)

# test
# n > 0     int
# n == 0    int
# n < 0     int

# n > 0     float
# n == 0    float
# n < 0     float


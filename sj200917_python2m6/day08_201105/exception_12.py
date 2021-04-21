"""
try...except...else

try:
    pass
except:
    pass
else:
    pass

Test
case 1: odd number 1
case 2: even number 4
case 3: even number 0

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

# except ZeroDivisionError as zde:
#     print("ZeroDivisionError")

else:
    reciprocal = 1 / num
    print(reciprocal)

# except ZeroDivisionError as zde:
#     print("ZeroDivisionError")




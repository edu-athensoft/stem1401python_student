"""
module 7. exception handling

Raise multiple exceptions
pay attention to the order in which exceptions raise

keyword:  assert

"""
print("Start")
try:
    num = int(input("Enter a number: "))
    if num <= 0:
        raise ValueError("That is not a positive number!")

    assert num % 2 == 0

except AssertionError as ae:
    print(ae)
    print("Not an even number!")

except ValueError as ve:
    print("ValueError Caught: ", ve, ve.args[0])

print("End")

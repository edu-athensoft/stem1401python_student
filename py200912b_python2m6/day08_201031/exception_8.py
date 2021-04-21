"""
try...except...else

to calculate the reciprocal of a number when it is an even number

keyword: assert

"""


try:
    num = int(input("Enter a number."))
    assert num % 2 == 0
except AssertionError as ae:
    print("this is an AssertionError")
    print(ae)
except Exception as e:
    # print("this is an AssertionError")
    print(e)
else:
    reciprocal = 1/num
    print(reciprocal)


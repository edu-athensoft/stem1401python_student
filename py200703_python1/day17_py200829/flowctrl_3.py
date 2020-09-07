"""
if-statement
if-else statement

if test_expr:
    statement(s)
else:
    statement(s)

"""

print("start!")
issunny = False

if issunny:
    print("hanging out and shopping.")
else:
    print("staying home and playing video games")

print("bye!")



# ex
# if a given number is greater than or equal to 0, then print out it is positive
# otherwise, print out it is negative

number = float(input("Enter an number: "))

if number >= 0:
    print("{} is a positive number".format(number))
else:
    print("{} is a negative number".format(number))


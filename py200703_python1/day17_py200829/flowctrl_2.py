"""
decision making

if-statement

if
else
elif
"""

# case 1. if-statement

"""
if test_expression:
    statement(s)
"""

print("start!")
issunny = True

if issunny:
    print("hanging out and shopping.")

print("bye!")


# ex.
# test if a given number is a positive number
# if yes, output a message of 'the {number} is a positive number'

"""
input('enter a number ')
positive = True

if positive:
    print("the number is a positive number")
"""

number = float(input('enter a number: '))

if number > 0:
    print("the {} is a positive number".format(number))

if number < 0:
    print("the {} is a positive number".format(number))
print()


# ex.
print("start!")
weather = input("Is it sunny today? [yes, no]:")

issunny = False
if weather == 'yes':
    issunny = True

if issunny:
    print("hanging out and shopping.")

print("bye!")
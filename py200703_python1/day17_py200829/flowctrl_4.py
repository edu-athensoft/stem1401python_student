"""
if-statement

if-elif-else statement

elif -> else if

if-elif,elif,...,else
"""

# sample

score = 89

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else:
    print("You got a F")


# ex.
# if a given number >0, output 'positive number'
# elif a given number ==0 , output 'zero'
# otherwise ,output 'negative number'

number = float(input("Enter a number: "))

if number > 0:
    print("{} is a positive number!".format(number))
elif number == 0:
    print("{} is zero!".format(number))
else:
    print("{} is a negative number!".format(number))

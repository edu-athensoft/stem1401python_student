"""
number >0 print out it's a positive number
number <0 print out it's a negative number
number ==0 print out it's zero
"""
import decimal as D
print(D.Decimal(0.0))

print(1.1+2.2 == 3.3)
print(D.Decimal(1.1))
print(D.Decimal(2.2))
print(D.Decimal(3.3))




# Kevin
number = -100
if number > 0:
    print("it's a positive number")
elif number < 0:
    print("it's a negative number")
else:
    print("it's zero")


# Ken
print("Number sign checker.")

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")




# Steven
num = int(input("Please enter a number:"))
if num > 0:
    print("It's a positive number")
elif num == 0:
    print("It's zero")
else:
    print("It's a negative number")


# Max

number = 1
if number >0:
    print("It is positive")
elif number <0:
    print("It is negative")
elif number == 0:
    print("It is zero")
else:
    print("Invalid")


#
# getting the input
num = input("Please input a number: ")
num = int(num)
# getting it's value

if num > 0:
    print("The number {} is a positive number.".format(num))
elif num < 0:
    print("The number {} is a negative number".format(num))
else:
    print("The number {} is zero".format(num))

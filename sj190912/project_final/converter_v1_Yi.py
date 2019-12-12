"""
app: unit converter
ver: 1
author: Yi
"""



def kilometers_miles(x):
    s = x * 0.621371
    return s

def miles_kilometers(x):
    s = x * 1.609344
    return s

def fahrenheit_celsius(x):
    s = (x - 32) * 5/9
    return s

def celsius_fahrenheit(x):
    s = (x * 9/5) + 32
    return s

def kilogram_pound(x):
    s = x * 2.20462
    return s

def pound_kilogram(x):
    s = x * 0.453592
    return s

def meter_foot(x):
    s = x * 3.28084
    return s

def foot_meter(x):
    s = x * 0.3048
    return s


print("1: Length or distance")
print("2: Temperature")
print("3: Weight")
print("4: Area")
choice = input("choice(1/2/3/4):")
if choice =='1':
    print("1: kilometers to miles:")
    print("2: miles to kilometers:")
    choice2 = input("choice(1/2):")
    if choice2 =='1':
        c = float(input("a number"))
        s = kilometers_miles(c)
        print("the number {} * 0.621371 = {}".format(c, s))
    if choice2 =='2':
        c = float(input("a number"))
        s = miles_kilometers(c)
        print("the number {} * 0.1.609344 = {}".format(c, s))
elif choice =='2':
    print("1: fahrenheit_celsius:")
    print("2: celsius_fahrenheit:")
    choice2 = input("choice(1/2):")
    if choice2 =='1':
        c = float(input("a number"))
        s = fahrenheit_celsius(c)
        print("the number {} - 32 * 5/9 = {}".format(c, s))
    if choice2 =='2':
        c = float(input("a number"))
        s = celsius_fahrenheit(c)
        print("the number ({} * 9/5) + 32 = {}".format(c, s))
elif choice == '3':
    print("1: kilogram_pound:")
    print("2: pound_kilogram:")
    choice2 = input("choice(1/2):")
    if choice2 =='1':
        c = float(input("a number"))
        s = kilogram_pound(c)
        print("the number {} * 2.20462 = {}".format(c, s))
    if choice2 =='2':
        c = float(input("a number"))
        s = pound_kilogram(c)
        print("the number {} * 0.453592 = {}".format(c, s))
elif choice == '4':
    print("1: meter_foot:")
    print("2: foot_meter:")
    choice2 = input("choice(1/2):")
    if choice2 =='1':
        c = float(input("a number"))
        s = meter_foot(c)
        print("the number {} * 3.28084 = {}".format(c, s))
    if choice2 =='2':
        c = float(input("a number"))
        s = foot_meter(c)
        print("the number {} * 0.3048 = {}".format(c, s))
else:
    print("this option does not exist.")
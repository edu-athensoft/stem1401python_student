"""
project_converter_v1_steven
"""

print("=== My Simple Converter ===")

print("1. Time")
print("2. Temperature")
print("3. Length or distance")
print()
choice1 = input("Please choose a converter type [1,2,3]:")

print("-------------------------------------------------------------------")
print()

if choice1 == "1":
    print("1. Minute -> Seconds")
    print("2. Minute -> Hours")
    print("3. Seconds -> Minutes")
    print("4. Seconds -> Hours")
    print("5. Hours -> Seconds")
    print("6. Hours -> Minutes")
    print()
    choice2 = input("Now, please choose a converting method:")

    print("-------------------------------------------------------------------")
    print()

    if choice2 == "1":
        a = input("Please enter the amount of minutes you would want to convert:")
        print(a, "minutes =", float(a) * 60, 'seconds')

    if choice2 == "2":
        a = input("Please enter the amount of minutes you would want to convert:")
        print(a, "minutes =", float(a) / 60, 'hours')

    if choice2 == "3":
        a = input("Please enter the amount of seconds you would want to convert:")
        print(a, "seconds =", float(a) / 60, 'minutes')

    if choice2 == "4":
        a = input("Please enter the amount of seconds you would want to convert:")
        print(a, "seconds =", float(a) / 3600, 'hours')

    if choice2 == "5":
        a = input("Please enter the amount of hours you would want to convert:")
        print(a, "hours =", float(a) * 3600, 'seconds')

    if choice2 == "6":
        a = input("Please enter the amount of hours you would want to convert:")
        print(a, "hours =", float(a) * 60, 'minutes')




if choice1 == "2":
    print("1. Celsius - Fahrenheit")
    print("2. Fahrenheit - Celsius")
    print()
    choice2 = input("Now, please choose a converting method:")

    print("-------------------------------------------------------------------")
    print()

    if choice2 == "1":
        b = input("Please enter the amount of Celsius you would want to convert:")
        print(b, u"\u2103", "=", float(b) * 1.8 + 32, u"\u2109")

    if choice2 == "2":
        b = input("Please enter the amount of Fahrenheit you would want to convert:")
        print(b, u"\u2109", "=", (float(b) - 32) / 1.8, u"\u2103")


if choice1 == "3":
    print("1. Meter - Kilometers")
    print("2. Meter - Miles")
    print("3. Kilometers - Meter")
    print("4. Kilometers - Miles")
    print("5. Miles - Meter")
    print("6. Miles - Kilometers")
    print()
    choice3 = input("Now, please choose a converting method:")

    print("-------------------------------------------------------------------")
    print()

    if choice3 == "1":
        c = input("Please enter the amount of meters you would want to convert:")
        print(c, "meters =", float(c) / 1000, 'kilometers')

    if choice3 == "2":
        c = input("Please enter the amount of meters you would want to convert:")
        print(c, "meters =", float(c) * 0.0006213712, 'miles')

    if choice3 == "3":
        c = input("Please enter the amount of kilometers you would want to convert:")
        print(c, "kilometers =", float(c) * 1000, 'meters')

    if choice3 == "4":
        c = input("Please enter the amount of kilometers you would want to convert:")
        print(c, "kilometers =", float(c) * 0.6213711922, 'miles')

    if choice3 == "5":
        c = input("Please enter the amount of miles you would want to convert:")
        print(c, "miles =", float(c) * 1609.344, 'meters')

    if choice3 == "6":
        c = input("Please enter the amount of miles you would want to convert:")
        print(c, "miles =", float(c) * 1.609344, 'kilometers')

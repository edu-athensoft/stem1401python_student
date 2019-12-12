

def kilometers_miles(x):
    result = x * 0.621371
    return result


def miles_kilometers(x):
    result = x * 1.60934
    return result


def fahrenheit_celsius(x):
    result = (x - 32) * 5/9
    return result


def celsius_fahrenheit(x):
    result = (x * 9/5) + 32
    return result


def kilogram_pound(x):
    result = x * 2.20462
    return result


def pound_kilogram(x):
    result = x * 0.453592
    return result


def meter_foot(x):
    result = x * 3.28084
    return result


def foot_meter(x):
    result = x * 0.3048
    return result


while(True):
    print("1: length or distance")
    print("2: temperature")
    print("3: weight")
    print("4: Area")
    choice = input("Chose one of the above:")
    if choice == "1":
        print("1: kilometers to miles")
        print("2: miles to kilometers")
        choice = input("Chose one of the above:")
        if choice == "1":
            number = float(input("Choose the number to convert:"))
            result = float(kilometers_miles(number))
            print("your converted unit is {:.2f} miles".format(result))
        if choice == "2":
            number = float(input("Choose the number to convert:"))
            result = float(miles_kilometers(number))
            print("your converted unit is {:.2f} kilometers".format(result))
    elif choice == "2":
        print("1: fahrenheit to celsius")
        print("2: celsius to fahrenheit")
        choice = input("Chose one of the above:")
        if choice == "1":
            number = float(input("Choose the number to convert:"))
            result = float(fahrenheit_celsius(number))
            print("your converted unit is {:.2f} celsius".format(result))
        if choice == "2":
            number = float(input("Choose the number to convert:"))
            result = float(celsius_fahrenheit(number))
            print("your converted unit is {:.2f} fahrenheit".format(result))
    elif choice == "3":
        print("1: kilogram to pound")
        print("2: pound to kilogram")
        choice = input("Chose one of the above:")
        if choice == "1":
            number = float(input("Choose the number to convert:"))
            result = float(kilogram_pound(number))
            print("your converted unit is {:.2f} pounds".format(result))
        if choice == "2":
            number = float(input("Choose the number to convert:"))
            result = float(pound_kilogram(number))
            print("your converted unit is {:.2f} kilograms".format(result))
    elif choice == "4":
        print("1: square meter to square foot")
        print("2: square foot to square meter")
        choice = input("Chose one of the above:")
        if choice == "1":
            number = float(input("Choose the number to convert:"))
            result = float(meter_foot(number))
            print("your converted unit is {:.2f} square feet".format(result))
        if choice == "2":
            number = float(input("Choose the number to convert:"))
            result = float(foot_meter(number))
            print("your converted unit is {:.2f} square meters".format(result))
    else:
        print("this option does not exist")


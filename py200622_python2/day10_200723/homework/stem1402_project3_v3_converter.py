"""
Project 3 || V2 || Max
Converter
"""
# Distance
def kilometers_miles(x):
    return x * 0.621
def miles_kilometers(x):
    return x * 1.609
# Temperature
def celsius_fahrenheit(x):
    return x * 1.8 + 32
def fahrenheit_celsius(x):
    return (x - 32) / 1.8
# Mass
def kilograms_pounds(x):
    return x * 2.205
def pounds_kilograms(x):
    return x * 0.454
# Area
def meter2_feet2(x):
    return x * 0.093
def feet2_meter2(x):
    return x * 10.764
# Volume
def litre_gallon(x):
    return x * 0.264
def gallon_litre(x):
    return x * 3.785
def gigabyte_gibibyte(x):
    return x * 0.931
def gibibyte_gigabyte(x):
    return x * 1.074
def menu2(unit1, unit2):
    global menu_2
    menu_2 = input("Please enter 1 for {0} to {1}, or 2 for {1} to {0} : ".format(unit1, unit2))
    while menu_2 != '1' or menu_2 != '2':
        if menu_2 == '1' or menu_2 == '2':
            break
        print("Sorry, that is not a valid choice. Please try again.")
        menu_2 = input("Please enter 1 for {0} to {1}, or 2 for {1} to {0} : ".format(unit1, unit2))
repeat = 1
if repeat:
    # Unit of measurement
    # Menu 1
    menu_1 = input("1. Distance \n2. Temperature \n3. Mass \n4. Area \n5. Volume \n6. Data storage: ")
    while menu_1 not in ['1', '2', '3', '4', '5', '6']:
        if menu_1 in ['1', '2', '3', '4', '5', '6']:
            break
        print("Sorry, that is not a valid choice. Please try again.")
        menu_1 = input("1. Distance \n2. Temperature \n3. Mass \n4. Area \n5. Volume \n6. Data storage: ")
    # Which conversion
    # Menu 2
    # Distance
    if menu_1 == '1':
        menu2("kilometers", "miles")
    # Temperature
    elif menu_1 == '2':
        menu2("celsius", "fahrenheit")
    # Mass
    elif menu_1 == '3':
        menu2("kilogram", "pound")
    # Area
    elif menu_1 == '4':
        menu2("square meter", "square foot")
    # Volume
    elif menu_1 == '5':
        menu2("litre", "gallon")
    elif menu_1 == '6':
        menu2("gigabyte", "gibibyte")
    # Their choice
    choice = menu_1 + menu_2
    # Amount
    amount = input("Please input the amount of units: ")
    try:
        float(amount)
    except ValueError:
        print("That is not a valid number. Please try again.")
        amount = int(input("Please input the amount of units: "))
    # Calculate
    # kilometers to miles
    if choice == '11':
        print("{} kilometers = {} miles".format(amount, kilometers_miles(amount)))
    # miles to kilometers
    elif choice == '12':
        print("{} miles = {} kilometers".format(amount, miles_kilometers(amount)))
    # celsius to fahrenheit
    elif choice == '21':
        print("{}\u00b0C = {}\u00b0F".format(amount, celsius_fahrenheit(amount)))
    # fahrenheit to celsius
    elif choice == '22':
        print("{}\u00b0F = {}\u00b0C".format(amount, fahrenheit_celsius(amount)))
    # kilograms to pounds
    elif choice == '31':
        print("{} kilograms = {} pounds".format(amount, kilograms_pounds(amount)))
    # pounds to kilograms
    elif choice == '32':
        print("{} pounds = {} kilograms".format(amount, pounds_kilograms(amount)))
    # square meters to square feet
    elif choice == '41':
        print("{} square meters = {} square feet".format(amount, meter2_feet2(amount)))
    # square feet to square meters
    elif choice == '42':
        print("{} square feet = {} square meters".format(amount, feet2_meter2(amount)))
    # litre to gallon
    elif choice == '51':
        print("{} litres = {} gallons".format(amount, litre_gallon(amount)))
    # gallon to litre
    elif choice == '52':
        print("{} gallons = {} litres ".format(amount, gallon_litre(amount)))
    # gigabyte to gibibyte
    elif choice == '61':
        print("{} gigabyte = {} gibibyte ".format(amount, gigabyte_gibibyte(amount)))
    # gibibyte to gigabyte
    elif choice == '62':
        print("{} gibibyte = {} gigabyte ".format(amount, gibibyte_gigabyte(amount)))
    repeat = input("Would you like to convert again? Please input 1 for Yes, or 2 for No: ")
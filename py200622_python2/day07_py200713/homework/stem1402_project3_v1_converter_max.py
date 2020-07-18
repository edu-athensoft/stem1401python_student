"""
Project 3 || V1 || Max
Converter
"""

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

# Unit of measurement
# Menu 1
menu_1 = input("Please input 1 for distance, 2 for temperature, 3 for mass, or 4 for area: ")

while menu_1 != '1' or menu_1 != '2' or menu_1 != '3' or menu_1 != '4':

    if menu_1 == '1' or menu_1 == '2' or menu_1 == '3' or menu_1 == '4':
        break

    print("Sorry, that is not a valid choice. Please try again.")
    menu_1 = input("Please input 1 for distance, 2 for temperature, 3 for mass, or 4 for area: ")

# Which conversion
# Menu 2
# Distance
if menu_1 == '1':
    menu_2 = input("Please enter 1 for kilometers to miles, or 2 for miles to kilometers : ")

    while menu_2 != '1' or menu_2 != '2':

        if menu_2 == '1' or menu_2 == '2':
            break
        print("Sorry, that is not a valid choice. Please try again.")
        menu_2 = input("Please enter 1 for kilometers to miles, or 2 for miles to kilometers : ")


# Temperature
elif menu_1 == '2':
    menu_2 = input("Please enter 1 for celsius to fahrenheit, or 2 for fahrenheit to celsius")

    while menu_2 != '1' or menu_2 != '2':

        if menu_2 == '1' or menu_2 == '2':
            break
        print("Sorry, that is not a valid choice. Please try again.")
        menu_2 = input("Please enter 1 for celsius to fahrenheit, or 2 for fahrenheit to celsius")


# Mass
elif menu_1 == '3':
    menu_2 = input("Please enter 1 for kilogram to pound, or 2 for pound to kilogram")

    while menu_2 != '1' or menu_2 != '2':

        if menu_2 == '1' or menu_2 == '2':
            break
        print("Sorry, that is not a valid choice. Please try again.")
        menu_2 = input("Please enter 1 for kilogram to pound, or 2 for pound to kilogram")


# Area
else:
    menu_2 = input("Please enter 1 for square meter to square foot, or square foot to square meter")

    while menu_2 != '1' or menu_2 != '2':

        if menu_2 == '1' or menu_2 == '2':
            break
        print("Sorry, that is not a valid choice. Please try again.")
        menu_2 = input("Please enter 1 for square meter to square foot, or square foot to square meter")

# Their choice
choice = menu_1 + menu_2

# Amount
amount = float(input("Please input the amount of units: "))

# Calculate
# Kilometers to miles
if choice == '11':
    print("{} kilometers = {} miles".format(amount, amount * 0.621))

# Miles to kilometers
elif choice == '12':
    print("{} miles = {} kilometers".format(amount, amount * 1.609))

# Celsius to fahrenheit
elif choice == '21':
    print("{}\u00b0C = {}\u00b0F".format(amount, amount * 1.8 + 32))

# fahrenheit to celsius
elif choice == '22':
    print("{}\u00b0F = {}\u00b0C".format(amount, (amount - 32) / 1.8))

# kilograms to pounds
elif choice == '31':
    print("{} kilograms = {} pounds".format(amount, amount * 2.205))

# pounds to kilograms
elif choice == '32':
    print("{} pounds = {} kilograms".format(amount, amount * 0.454))

# square meters to square feet
elif choice == '41':
    print("{} square meters = {} square feet".format(amount, amount * 0.093))

# square feet to square meters
elif choice == '42':
    print("{} square meters = {} square feet".format(amount, amount * 10.764))

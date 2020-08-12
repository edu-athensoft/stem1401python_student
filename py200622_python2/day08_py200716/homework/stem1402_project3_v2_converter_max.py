"""
Project 3 || V1 || Max
Converter
"""


# Distance1
# km to meter
def km_m(x):
    return x * 0.621


def m_km(x):
    return x * 1.609


# Temperature
# celsuis to fr
def c_f(x):
    return x * 1.8 + 32

#
def f_c(x):
    return (x - 32) / 1.8


# Mass
def kg_lbs(x):
    return x * 2.205


def lbs_kg(x):
    return x * 0.454


# Area
def m2_f2(x):
    return x * 0.093


def f2_m2(x):
    return x * 10.764


def menu2(unit1, unit2):
    global menu_2
    menu_2 = input("Please enter 1 for {0} to {1}, or 2 for {1} to {0} : ".format(unit1, unit2))

    while menu_2 != '1' or menu_2 != '2':

        if menu_2 == '1' or menu_2 == '2':
            break
        print("Sorry, that is not a valid choice. Please try again.")
        menu_2 = input("Please enter 1 for {0} to {1}, or 2 for {1} to {0} : ".format(unit1, unit2))


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
    menu2("kilometers", "miles")

# Temperature
elif menu_1 == '2':
    menu2("celsius", "fahrenheit")

# Mass
elif menu_1 == '3':
    menu2("kilogram", "pound")

# Area
else:
    menu2("square meter", "square foot")

# Their choice
choice = menu_1 + menu_2

# Amount
amount = float(input("Please input the amount of units: "))

# Calculate
# Kilometers to miles
if choice == '11':
    print("{} kilometers = {} miles".format(amount, km_m(amount)))

# Miles to kilometers
elif choice == '12':
    print("{} miles = {} kilometers".format(amount, m_km(amount)))

# Celsius to fahrenheit
elif choice == '21':
    print("{}\u00b0C = {}\u00b0F".format(amount, c_f(amount)))

# fahrenheit to celsius
elif choice == '22':
    print("{}\u00b0F = {}\u00b0C".format(amount, f_c(amount)))

# kilograms to pounds
elif choice == '31':
    print("{} kilograms = {} pounds".format(amount, kg_lbs(amount)))

# pounds to kilograms
elif choice == '32':
    print("{} pounds = {} kilograms".format(amount, lbs_kg(amount)))

# square meters to square feet
elif choice == '41':
    print("{} square meters = {} square feet".format(amount, m2_f2(amount)))

# square feet to square meters
elif choice == '42':
    print("{} square meters = {} square feet".format(amount, f2_m2(amount)))

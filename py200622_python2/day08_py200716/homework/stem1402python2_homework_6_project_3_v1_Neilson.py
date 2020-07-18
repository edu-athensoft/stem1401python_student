"""
Project_3
menu 2
"""

"""
km_m

km to meter ?
km to mile ?
"""


# Time
def min_hour(x):
    return x / 60


def min_sec(x):
    return x * 60


def hour_min(x):
    return x * 60


def hour_sec(x):
    return x * 3600


def sec_hour(x):
    return x / 3600


def sec_min(x):
    return x / 60


# Temperature
def celsius_fahrenheit(x):
    return (x * 1.8) + 32


def celsius_kelvin(x):
    return x + 273.15


def fahrenheit_celsius(x):
    return (x - 32) * 1.8


def fahrenheit_kelvin(x):
    return (x - 32) * 1.8 + 273.15


def kelvin_celsius(x):
    return x - 273.15


def kelvin_fahrenheit(x):
    return (x - 273.15) * 1.8 + 32


# Weight
def kg_g(x):
    return x * 1000


def kg_pound(x):
    return x * 2.205


def g_kg(x):
    return x / 1000


def g_pound(x):
    return x / 1000 * 2.205


def pound_kg(x):
    return x / 2.205


def pound_g(x):
    return x / 2.205 * 1000


# Time choice

def time():
    print()
    print("===Time converter===")
    print("Press 1 for minute to hour")
    print("Press 2 for minute to second")
    print("Press 3 for hour to minute")
    print("Press 4 for hour to second")
    print("Press 5 for second to hour")
    print("Press 6 for second to minute")
    choice_2 = int(input("Now please input you choice: "))
    if choice_2 == 1:
        user_input = float(input("Please input the amount of minutes to convert: "))
        print(f"If you convert {user_input} minutes into hours you get {min_hour(user_input)} hours.")
    elif choice_2 == 2:
        user_input = float(input("Please input the amount of minutes to convert: "))
        print(f"If you convert {user_input} minutes into seconds you get {min_sec(user_input)} seconds.")
    elif choice_2 == 3:
        user_input = float(input("Please input the amount of hours to convert: "))
        print(f"If you convert {user_input} hours into minutes you get {hour_min(user_input)} minutes.")
    elif choice_2 == 4:
        user_input = float(input("Please input the amount of hours to convert: "))
        print(f"If you convert {user_input} hours into seconds you get {hour_sec(user_input)} seconds.")
    elif choice_2 == 5:
        user_input = float(input("Please input the amount of seconds to convert: "))
        print(f"If you convert {user_input} seconds into minutes you get {sec_min(user_input)} minutes.")
    elif choice_2 == 6:
        user_input = float(input("Please input the amount of seconds to convert: "))
        print(f"If you convert {user_input} seconds into hours you get {sec_hour(user_input)} hours.")
    else:
        print("Error")


# Temperature choice

def temperature():
    print()
    print("===Temperature converter===")
    print("Press 1 for celsius to fahrenheit")
    print("Press 2 for celsius to kelvin")
    print("Press 3 for fahrenheit to celsius")
    print("Press 4 for fahrenheit to kelvin")
    print("Press 5 for kelvin to celsius")
    print("Press 6 for kelvin to fahrenheit")
    choice_2 = int(input("Now please input you choice: "))
    if choice_2 == 1:
        user_input = float(input("Please input the amount of kg to convert: "))
        print(
            f"If you convert {user_input} celsius into fahrenheit you get {celsius_fahrenheit(user_input)} fahrenheit.")
    elif choice_2 == 2:
        user_input = float(input("Please input the amount of kg to convert: "))
        print(f"If you convert {user_input} celsius into kelvin you get {celsius_kelvin(user_input)} kelvin.")
    elif choice_2 == 3:
        user_input = float(input("Please input the amount of g to convert: "))
        print(f"If you convert {user_input} fahrenheit into celsius you get {fahrenheit_celsius(user_input)} celsius.")
    elif choice_2 == 4:
        user_input = float(input("Please input the amount of g to convert: "))
        print(f"If you convert {user_input} fahrenheit into kelvin you get {fahrenheit_kelvin(user_input)} kelvin.")
    elif choice_2 == 5:
        user_input = float(input("Please input the amount of pounds to convert: "))
        print(f"If you convert {user_input} kelvin into celsius you get {kelvin_celsius(user_input)} celsius.")
    elif choice_2 == 6:
        user_input = float(input("Please input the amount of pounds to convert: "))
        print(f"If you convert {user_input} kelvin into fahrenheit you get {kelvin_fahrenheit(user_input)} fahrenheit.")
    else:
        print("Error")


# Weight choice

def weight():
    print()
    print("===Weight converter===")
    print("Press 1 for kg to g")
    print("Press 2 for kg to pound")
    print("Press 3 for g to kg")
    print("Press 4 for g to pound")
    print("Press 5 for pound to kg")
    print("Press 6 for pound to g")
    choice_2 = int(input("Now please input you choice: "))
    if choice_2 == 1:
        user_input = float(input("Please input the amount of kg to convert: "))
        print(f"If you convert {user_input} kg into g you get {kg_g(user_input)} g.")
    elif choice_2 == 2:
        user_input = float(input("Please input the amount of kg to convert: "))
        print(f"If you convert {user_input} kg into pounds you get {kg_pound(user_input)} pounds.")
    elif choice_2 == 3:
        user_input = float(input("Please input the amount of g to convert: "))
        print(f"If you convert {user_input} g into kg you get {g_kg(user_input)} kg.")
    elif choice_2 == 4:
        user_input = float(input("Please input the amount of g to convert: "))
        print(f"If you convert {user_input} g into pounds you get {g_pound(user_input)} pounds.")
    elif choice_2 == 5:
        user_input = float(input("Please input the amount of pounds to convert: "))
        print(f"If you convert {user_input} pounds into kg you get {pound_kg(user_input)} kg.")
    elif choice_2 == 6:
        user_input = float(input("Please input the amount of pounds to convert: "))
        print(f"If you convert {user_input} pounds into g you get {pound_kg(user_input)} g.")
    else:
        print("Error")


print("===Simple Converter===")
print("Press 1 for time conversion")
print("Press 2 for temperature conversion")
print("Press 3 for weight conversion")
choice_1 = int(input("Please input your choice: "))
if choice_1 == 1:
    time()
elif choice_1 == 2:
    temperature()
elif choice_1 == 3:
    weight()
else:
    print("Error")

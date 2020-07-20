"""
project_converter_v1.2_steven
"""


# Kilograms, Tons, Grams

def kg_g(x):
    return x * 1000

def kg_t(x):
    return x * 0.001

def g_kg(x):
    return x / 1000

def g_t(x):
    return x * 0.000001

def t_kg(x):
    return x / 0.001

def t_g(x):
    return x / 0.000001


# CAD, USD

def C_U(x):
    return x * 0.74

def U_C(x):
    return x * 1.36


# Minutes, Seconds, Hours

def min_sec(x):
    return x * 60

def min_hour(x):
    return x / 60

def sec_min(x):
    return x / 60

def sec_hour(x):
    return x / 3600

def hour_min(x):
    return x * 60

def hour_sec(x):
    return x * 3600


# Celsius, Fahrenheit

def c_f(x):
    return x * 1.8 + 32

def f_c(x):
    return (x - 32) / 1.8


# Meters, Kilometers, Miles

def m_k(x):
    return x / 1000

def m_mi(x):
    return x * 0.0006213712

def k_m(x):
    return x * 1000

def k_mi(x):
    return x * 0.6213711922

def mi_m(x):
    return x * 1609.344

def mi_k(x):
    return x * 1.609344




print("=== My Simple Converter ===")
print()

print("1. Time")
print("2. Temperature")
print("3. Length or distance")
print("4. Currency")
print("5. Mass or Weight")
print()
choice1 = input("Please choose the number of converter type:")

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
    choice2 = input("Now, please choose the number of the converting method:")

    print("-------------------------------------------------------------------")
    print()

    if choice2 == "1":
        a = float(input("Please enter the amount of minutes you would want to convert:"))
        print(f"{a} minutes = {min_sec(a)} seconds")

    if choice2 == "2":
        a = float(input("Please enter the amount of minutes you would want to convert:"))
        print(f"{a} minutes = {min_hour(a):.2f} hours")

    if choice2 == "3":
        a = float(input("Please enter the amount of seconds you would want to convert:"))
        print(f"{a} seconds = {sec_min(a):.2f} minutes")

    if choice2 == "4":
        a = float(input("Please enter the amount of seconds you would want to convert:"))
        print(f"{a} seconds = {sec_hour(a):.2f} hours")

    if choice2 == "5":
        a = float(input("Please enter the amount of hours you would want to convert:"))
        print(f"{a} hours = {hour_sec(a)} seconds")

    if choice2 == "6":
        a = float(input("Please enter the amount of hours you would want to convert:"))
        print(f"{a} hours = {hour_min(a)} minutes")



if choice1 == "2":
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print()
    choice2 = input("Now, please choose the number of converting method:")

    print("-------------------------------------------------------------------")
    print()

    if choice2 == "1":
        b = float(input("Please enter the amount of Celsius you would want to convert:"))
        print(f'{b} \u2103 = {c_f(b)} \u2109')

    if choice2 == "2":
        b = float(input("Please enter the amount of Fahrenheit you would want to convert:"))
        print(f'{b} \u2109 = {f_c(b):.2f} \u2103')



if choice1 == "3":
    print("1. Meter -> Kilometers")
    print("2. Meter -> Miles")
    print("3. Kilometers -> Meter")
    print("4. Kilometers -> Miles")
    print("5. Miles -> Meter")
    print("6. Miles -> Kilometers")
    print()
    choice3 = input("Now, please choose the number of the converting method:")

    print("-------------------------------------------------------------------")
    print()

    if choice3 == "1":
        c = float(input("Please enter the amount of meters you would want to convert:"))
        print(f"{c} meters = {m_k(c)} kilometers")

    if choice3 == "2":
        c = float(input("Please enter the amount of meters you would want to convert:"))
        print(f"{c} meters = {m_mi(c)} miles")

    if choice3 == "3":
        c = float(input("Please enter the amount of kilometers you would want to convert:"))
        print(f"{c} kilometers = {k_m(c):.2f} meters")

    if choice3 == "4":
        c = float(input("Please enter the amount of kilometers you would want to convert:"))
        print(f"{c} kilometers = {k_mi(c):.2f} miles")

    if choice3 == "5":
        c = float(input("Please enter the amount of miles you would want to convert:"))
        print(f"{c} miles = {mi_m(c):.2f} meters")

    if choice3 == "6":
        c = float(input("Please enter the amount of miles you would want to convert:"))
        print(f"{c} miles = {mi_k(c):.2f} kilometers")



if choice1 == "4":
    print("1. CAD -> USD")
    print("2. USD -> CAD")
    print()
    choice3 = input("Now, please choose the number of the converting method:")

    print("-------------------------------------------------------------------")
    print()

    if choice3 == "1":
        d = float(input("Please enter the amount of CAD you would want to convert:"))
        print(f"{d} CAD = {C_U(d):.2f} USD")

    if choice3 == "2":
        d = float(input("Please enter the amount of USD you would want to convert:"))
        print(f"{d} USD = {U_C(d):.2f} CAD")



if choice1 == "5":
    print("1. Kilograms -> Grams")
    print("2. Kilometers -> Tons")
    print("3. Grams -> Kilograms")
    print("4. Grams -> Tons")
    print("5. Tons -> Kilograms")
    print("6. Tons -> Grams")
    print()
    choice3 = input("Now, please choose the number of the converting method:")

    print("-------------------------------------------------------------------")
    print()

    if choice3 == "1":
        e = float(input("Please enter the amount of kilogram you would want to convert:"))
        print(f"{e} kg = {kg_g(e):.2f} g")

    if choice3 == "2":
        e = float(input("Please enter the amount of kilogram you would want to convert:"))
        print(f"{e} kg = {kg_t(e):.2f} t")

    if choice3 == "3":
        e = float(input("Please enter the amount of gram you would want to convert:"))
        print(f"{e} g = {g_kg(e):.2f} kg")

    if choice3 == "4":
        e = float(input("Please enter the amount of gram you would want to convert:"))
        print(f"{e} g = {g_t(e):.2f} t")

    if choice3 == "5":
        e = float(input("Please enter the amount of ton you would want to convert:"))
        print(f"{e} t = {t_kg(e):.2f} kg")

    if choice3 == "6":
        e = float(input("Please enter the amount of ton you would want to convert:"))
        print(f"{e} t = {t_g(e):.2f} g")











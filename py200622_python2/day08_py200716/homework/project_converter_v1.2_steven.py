"""
project_converter_v1.2_steven
"""


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
        # apply string formatting
        print(f"{a} minutes = {min_hour(a):.2f} hours")
        # print(f"{a} minutes = {min_hour(a)} hours")

    if choice2 == "3":
        a = float(input("Please enter the amount of seconds you would want to convert:"))
        print(f"{a} seconds = {sec_min(a)} minutes")

    if choice2 == "4":
        a = float(input("Please enter the amount of seconds you would want to convert:"))
        print(f"{a} seconds = {sec_hour(a)} hours")

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
        print(f'{b} \u2109 = {f_c(b)} \u2103')



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
        print(f"{c} kilometers = {k_m(c)} meters")

    if choice3 == "4":
        c = float(input("Please enter the amount of kilometers you would want to convert:"))
        print(f"{c} kilometers = {k_mi(c)} miles")

    if choice3 == "5":
        c = float(input("Please enter the amount of miles you would want to convert:"))
        print(f"{c} miles = {mi_m(c)} meters")

    if choice3 == "6":
        c = float(input("Please enter the amount of miles you would want to convert:"))
        print(f"{c} miles = {mi_k(c)} kilometers")
















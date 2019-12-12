"""
app: unit converter
ver: 1
author: Yun Gong Zhang
"""


selection = int(input("Welcome to Operation: Convertion. Choose a converter type! \n"
                      "1. Length \n"
                      "2. Temperature \n"
                      "3. Weight \n"
                      "6. Area \n"))

if selection == 1:
    selection2 = int(input("Good choice! \n"
                           "1. kilometers to miles \n"
                           "2. miles to kilometers \n"))
    if selection2 == 1:
        x = int(input("What do you want to convert? \n"
                      ""))
        y = x*0.621371
        print("{} km is equal to {} miles". format(x, y))

    if selection2 == 2:
        x = int(input("What do you want to convert? \n"
                      ""))
        y = x*1.609344
        print("{} miles is equal to {} km".format(x, y))

if selection == 2:
    selection3 = int(input("Good choice! \n"
                           "1. Celsius to Fahrenheit\n"
                           "2. Fahrenheit to Celsius \n"))
    if selection3 == 1:
        x = int(input("What temperature do you want to convert? \n"
                      ""))
        y = x*33.8
        print("{}°C is equal to {}°F". format(x, y))

    if selection3 == 2:
        x = int(input("What temperature do you want to convert? \n"
                      ""))
        y = x*33.8
        print("{}°C is equal to {}°F". format(x, y))

if selection == 3:
    selection4 = int(input("Good choice! \n"
                           "1. Kilogram to Pound\n"
                           "2. Pound to Kilogram \n"))
    if selection4 == 1:
        x = int(input("What weight do you want to convert? \n"
                      ""))
        y = x*2.20462262
        print("{} kg is equal to {} pounds". format(x, y))

    if selection4 == 2:
        x = int(input("What temperature do you want to convert? \n"
                      ""))
        y = x*0.45359237
        print("{} pounds is equal to {} kg". format(x, y))

if selection == 4:
    selection5 = int(input("Good choice! \n"
                           "1. Square meter to Square foot\n"
                           "2. Square foot to Square meter \n"))
    if selection5 == 1:
        x = int(input("What do you want to convert? \n"
                      ""))
        y = x*10.7639104
        print("{} square meter is equal to {}". format(x, y))

    if selection5 == 2:
        x = int(input("What do you want to convert? \n"
                      ""))
        y = x*0.09290304
        print("{} square foot is equal to {} square meter". format(x, y))
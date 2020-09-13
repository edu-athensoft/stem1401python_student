"""
app: unit converter
version: 3.0
author: YouRan Wang
"""


def km_to_mile(x):
    result = round(x / 1.609, 3)
    print("\n{} km = around {} miles".format(x, result))


def mile_to_km(x):
    result = round(x * 1.609, 3)
    print("\n{} miles = around {} km".format(x, result))


def celsius_to_fahrenheit(x):
    result = round(x * 9 / 5 + 32, 3)
    print("\n{} Celsius = around {} Fahrenheit".format(x, result))


def fahrenheit_to_celsius(x):
    result = round((x - 32) * (5 / 9), 3)
    print("\n{} Fahrenheit  = around {} Celsius".format(x, result))


def kilogram_to_pound(x):
    result = round(x * 2.205, 3)
    print("\n{} Kilogram = around {} Pound".format(x, result))


def pound_to_kilogram(x):
    result = round(x / 2.205, 3)
    print("\n{} Pound  = around {} Kilogram".format(x, result))


def square_meters_to_square_feet(x):
    result = round(x * 10.764, 3)
    print("\n{} Square Meters = around {} Square Feet".format(x, result))


def square_feet_to_square_meters(x):
    result = round(x / 10.764, 3)
    print("\n{} Square Feet  = around {} Square Meters".format(x, result))


def cd_to_usd(x):
    result = round(x * 0.76, 3)
    print("\n{} CND = around {} USD".format(x, result))


def usd_to_cd(x):
    result = round(x * 1.33, 3)
    print("\n{} USD  = around {} CD".format(x, result))


def cd_to_yuan(x):
    result = round(x * 5.3, 3)
    print("\n{} CD = around {} Yuan".format(x, result))


def yuan_to_cd(x):
    result = round(x * 0.19, 3)
    print("\n{} Yuan = around {} CD".format(x, result))


def us_to_yuan(x):
    result = round(x * 6.97, 3)
    print("\n{} US = around {} Yuan".format(x, result))


def yuan_to_us(x):
    result = round(x * 0.14, 3)
    print("\n{} Yuan = around {} CD".format(x, result))


def length_part():
    flag5 = True
    while flag5:
        print("1 = Kilometers to Miles \n"
              "2 = Miles to Kilometers \n"
              "exit = back \n")
        y = (input("input your choice: ")).lower()
        my_input_value = int(input("Input your the value you want to convert: "))
        if y == "1":
            km_to_mile(my_input_value)
        elif y == "2":
            mile_to_km(my_input_value)
        elif y == "exit":
            flag5 = False
        else:
            print("\nplease select an actual choice man!!!")
            length_part()


def temperature_part():
    flag5 = True
    while flag5:
        print("1 = Celsius to Fahrenheit \n"
              "2 = Fahrenheit to Celsius \n"
              "exit = back \n")
        y = (input("input your choice: ")).lower()
        input_value = int(input("Input your the value you want to convert: "))
        if y == "1":
            celsius_to_fahrenheit(input_value)
        elif y == "2":
            fahrenheit_to_celsius(input_value)
        elif z == "exit":
            flag5 = False
        else:
            print("\nplease select an actual choice man!!!")
            temperature_part()


def weight_part():
    flag4 = True
    while flag4:
        print("1 = Kilogram to Pound \n"
              "2 = Pound to Kilogram \n"
              "exit = back \n")
        x = (input("input your choice: ")).lower()
        input_value = int(input("Input your the value you want to convert: "))
        if x == "1":
            kilogram_to_pound(int(input("Input your value")))
        elif x == "2":
            pound_to_kilogram(int(input("Input your value")))
        elif z == "exit":
            flag4 = False
        else:
            print("\nplease select an actual choice man!!!")
            weight_part()


def area_part():
    flag3 = True
    while flag3:
        print("1 = Square Meters to Square Feet \n"
              "2 = Square Feet to Square Meters \n"
              "exit = back \n")
        x = (input("input your choice: ")).lower()
        input_value = int(input("Input your the value you want to convert: "))
        if x == "1":
            square_meters_to_square_feet(input_value)
        elif x == "2":
            square_feet_to_square_meters(input_value)
        elif z == "exit":
            flag3 = False
        else:
            print("\nplease select an actual choice man!!!")
            area_part()


def money_part():
    flag2 = True
    while flag2:
        print("1 = Canadian to US \n" +
              "2 = US to Canadian \n"  +
              "3 = Canadian to Chinese \n"  +
              "4 = Chinese to Canadian \n"  +
              "5 = US to Chinese \n"   +
              "6 = Chinese to US \n"  +
              "exit = back \n")
        x = (input("input your choice: ")).lower()

        if x == "1":
            input_value = int(input("Input your the value you want to convert: money_part()"))
            cd_to_usd(input_value)
        elif x == "2":
            input_value = int(input("Input your the value you want to convert: money_part()"))
            usd_to_cd(input_value)
        elif x == "3":
            input_value = int(input("Input your the value you want to convert: money_part()"))
            cd_to_yuan(input_value)
        elif x == "4":
            input_value = int(input("Input your the value you want to convert: money_part()"))
            yuan_to_cd(input_value)
        elif x == "5":
            input_value = int(input("Input your the value you want to convert: money_part()"))
            usd_to_cd(input_value)
        elif x == "6":
            input_value = int(input("Input your the value you want to convert: money_part()"))
            usd_to_cd(input_value)
        elif x == "exit":
            print("exit to main menu money_part()")
            break;

        else:
            print("\nplease select an actual choice man!!!")
            # money_part()


flag = True
while flag:
    print("\n1 = Length converter \n"
          "2 = Temperature converter \n"
          "3 = Weight converter \n"
          "4 = Area converter \n"
          "5 = Currency converter \n"
          "exit = stop program \n")

    z = input("input your choice: ").lower()
    if z == "1":
        length_part()
    elif z == "2":
        temperature_part()
    elif z == "3":
        weight_part()
    elif z == "4":
        area_part()
    elif z == "5":
        money_part()
    elif z == "exit":
        flag = False
    else:
        print("\nplease select an actual choice man!!!")

# money_part()
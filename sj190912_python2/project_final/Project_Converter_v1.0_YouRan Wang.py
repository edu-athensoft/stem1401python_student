"""
app: unit converter
version: 1.0
author: YouRan Wang
"""


def length():
    print("1 = Kilometers to Miles \n"
          "2 = Miles to Kilometers")
    x = 0
    x = int(input("input your choice: "))
    y = 0
    if x == 1:
        y = int(input("input your number: "))
        result = round(y / 1.609, 3)
        print("{} km = around {} miles".format(y, result))
    elif x == 2:
        y = int(input("input your number: "))
        result = round(y * 1.609, 3)
        print("{} miles = around {} km".format(y, result))
    else:
        print(" please select an actual choice man")
        length()


def temperature():
    print("1 = Celsius to Fahrenheit \n"
          "2 = Fahrenheit to Celsius")
    x = 0
    x = int(input("input your choice: "))
    y = 0
    if x == 1:
        y = int(input("input your number: "))
        result = round(y * 9/5 + 32, 3)
        print("{} Celsius = around {} Fahrenheit".format(y, result))
    elif x == 2:
        y = int(input("input your number: "))
        result = round((y - 32) * (5/9), 3)
        print("{} Fahrenheit  = around {} Celsius".format(y, result))
    else:
        print(" please select an actual choice man")
        temperature()


def weight():
    print("1 = Kilogram to Pound \n"
          "2 = Pound to Kilogram")
    x = 0
    x = int(input("input your choice: "))
    y = 0
    if x == 1:
        y = int(input("input your number: "))
        result = round(y * 2.205, 3)
        print("{} Kilogram = around {} Pound".format(y, result))
    elif x == 2:
        y = int(input("input your number: "))
        result = round(y / 2.205, 3)
        print("{} Pound  = around {} Kilogram".format(y, result))
    else:
        print(" please select an actual choice man")
        weight()


def area():
    print("1 = Square Meters to Square Feet \n"
          "2 = Square Feet to Square Meters")
    x = 0
    x = int(input("input your choice: "))
    y = 0
    if x == 1:
        y = int(input("input your number: "))
        result = round(y * 10.764, 3)
        print("{} Square Meters = around {} Square Feet".format(y, result))
    elif x == 2:
        y = int(input("input your number: "))
        result = round(y / 10.764, 3)
        print("{} Square Feet  = around {} Square Meters".format(y, result))
    else:
        print(" please select an actual choice man")
        area()


print("1 = Length Converter \n"
      "2 = Temperature Converter \n"
      "3 = weight converter \n"
      "4 = area converter \n")
z = 0
z = int(input("input your choice: "))
if z == 1:
    length()
elif z == 2:
    temperature()
elif z == 3:
    weight()
elif z == 4:
    area()
else:
    print(" bro u serious??")
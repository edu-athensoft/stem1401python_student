"""
app: unit converter
ver: 3
author: Yi
"""



def kilometers_miles(x):
    s = x * 0.621371
    return s

def miles_kilometers(x):
    s = x * 1.609344
    return s

def fahrenheit_celsius(x):
    s = (x - 32) * 5/9
    return s

def celsius_fahrenheit(x):
    s = (x * 9/5) + 32
    return s

def kilogram_pound(x):
    s = x * 2.20462
    return s

def pound_kilogram(x):
    s = x * 0.453592
    return s

def meter_foot(x):
    s = x * 3.28084
    return s

def foot_meter(x):
    s = x * 0.3048
    return s

def metre_milimetre(x):
    s = x * 1000
    return s

def milimeter_meter(x):
    s = x / 1000
    return s

def milimetrecarre_metrecarre(x):
    s = x / 10000000
    return s

def metrecarre_milimetrecarre(x):
    s = x * 10000000
    return s

def foot_inch(x):
    s = x * 12
    return s

def inch_foot(x):
    s = x / 12
    return s

def inch_cm(x):
    s = x * 2.54
    return s

def cm_inch(x):
    s = x / 2.54
    return s

def inch_mm(x):
    s = x * 25.4
    return s

def mm_inch(x):
    s = x / 25.4
    return s

def CAD_CNY(x):
    s = x * 5.34
    return s

def CNY_CAD(x):
    s = x / 5.34
    return s


f = True
while (f):
    print("Converte calculer")
    print("0: Exit to the converter")
    print("1: Length or distance")
    print("2: Temperature")
    print("3: Weight")
    print("4: Area")
    print("5: Currency")
    choice = input("choice(0/1/2/3/4/5):")

    if choice == "0":
        print("Over")
        break
    elif choice >= "6":
        print("this option does not exist.")
        continue
    elif choice <= "0":
        print("this option does not exist.")
        continue

    if choice =='1':
        while True:
          print("0: exit to main menu:")
          print("1: kilometers to miles:")
          print("2: miles to kilometers:")
          print("3: metre to milimeter:")
          print("4: milimetre to meter:")
          print("5: metrecarre to milimetercarre:")
          print("6: milimetrecarre to metercarre:")
          print("7: foot to inch:")
          print("8: inch to foot:")
          print("9: inch to cm:")
          print("10: cm to inch:")
          print("11: inch to mm:")
          print("12: mm to inch:")
          choice2 = input("choice(0/1/2/3/4/5/6/7/8/9/10/11/12):")
          if choice2 =='1':
              c = float(input("a number:"))
              km2mile = kilometers_miles(c)
              print("the number {} * 0.621371 = {}".format(c, km2mile))
          if choice2 =='2':
              c = float(input("a number:"))
              mile2km = miles_kilometers(c)
              print("the number {} * 0.1.609344 = {}".format(c, mile2km))
          if choice2 =='3':
              c = float(input("a number:"))
              m2mili = metre_milimetre(c)
              print("the number {} * 1000 = {}".format(c, m2mili))
          if choice2 == '4':
              c = float(input("a number"))
              mili2m = milimeter_meter(c)
              print("the number {} / 1000 = {}".format(c, mili2m))
          if choice2 == '5':
              c = float(input("a number:"))
              mc2milic = metrecarre_milimetrecarre(c)
              print("the number {} * 10000000 = {}".format(c, mc2milic))
          if choice2 == '6':
              c = float(input("a number:"))
              milic2mc = milimetrecarre_metrecarre(c)
              print("the number {} / 10000000 = {}".format(c, milic2mc))
          if choice2 == '7':
              c = float(input("a number:"))
              f2i = foot_inch(c)
              print("the number {} * 12 = {}".format(c, f2i))
          if choice2 == '8':
              c = float(input("a number:"))
              i2f = inch_foot(c)
              print("the number {} / 12 = {}".format(c, i2f))
          if choice2 == '9':
              c = float(input("a number:"))
              i2cm = inch_cm(c)
              print("the number {} * 2.54 = {}".format(c, i2cm))
          if choice2 == '10':
              c = float(input("a number:"))
              cm2i = cm_inch(c)
              print("the number {} / 2.54 = {}".format(c, cm2i))
          if choice2 == '11':
              c = float(input("a number:"))
              i2mm = inch_mm(c)
              print("the number {} * 25.4 = {}".format(c, i2mm))
          if choice2 == '12':
              c = float(input("a number:"))
              mm2i = mm_inch(c)
              print("the number {} / 25.4 = {}".format(c, mm2i))
          if choice2 == "0":
              break
    elif choice =='2':
      print("0: exit to main menu:")
      print("1: fahrenheit_celsius:")
      print("2: celsius_fahrenheit:")
      choice2 = input("choice(0/1/2):")
      if choice2 =='1':
        c = float(input("a number:"))
        f2c = fahrenheit_celsius(c)
        print("the number {} - 32 * 5/9 = {}".format(c, f2c))
      if choice2 =='2':
        c = float(input("a number:"))
        c2f = celsius_fahrenheit(c)
        print("the number ({} * 9/5) + 32 = {}".format(c, c2f))
      if input == "0":
          break
    elif choice == '3':
      print("0: exit to main menu:")
      print("1: kilogram_pound:")
      print("2: pound_kilogram:")
      choice2 = input("choice(0/1/2):")
      if choice2 =='1':
          c = float(input("a number:"))
          k2p = kilogram_pound(c)
          print("the number {} * 2.20462 = {}".format(c, k2p))
      if choice2 =='2':
          c = float(input("a number:"))
          p2k = pound_kilogram(c)
          print("the number {} * 0.453592 = {}".format(c, p2k))
      if input == "0":
          break
    elif choice == '4':
      print("0: exit to main menu:")
      print("1: meter_foot:")
      print("2: foot_meter:")
      choice2 = input("choice(0/1/2):")
      if choice2 =='1':
          c = float(input("a number:"))
          m2f = meter_foot(c)
          print("the number {} * 3.28084 = {}".format(c, m2f))
      if choice2 =='2':
          c = float(input("a number:"))
          f2m = foot_meter(c)
          print("the number {} * 0.3048 = {}".format(c, f2m))
      if input == "0":
          break
    elif choice == "5":
      print("0: exit to main menu:")
      print("1: CAD_CNY")
      print("2: CNY_CAD")
      choice2 = input("choice(0/1/2):")
      if choice2 =='1':
          c = float(input("a number:"))
          CAD2CNY = CAD_CNY(c)
          print("the number {} * 5.34 = {}".format(c, CAD2CNY))
      if choice2 =='2':
          c = float(input("a number:"))
          CNY2CAD = CNY_CAD(c)
          print("the number {} / 5.34 = {}".format(c, CNY2CAD))
      if input == "0":
          break
else:
    print("this option does not exist.")

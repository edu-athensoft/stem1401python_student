"""
For June 23rd, 2020.
project_converter_v4_ken
Converter v4
"""

"""
Simple unit converter works by using nested if and elif statements in order to read the type of 
conversion (eg. distance) chosen through the input question. 
Then this is done again for the order of conversion (eg. km to miles.

f strings are used to simplify the strings and the calculations (conversions) are made directly in the print function.

If the user inputs a choice that isn't available, the program restarts.
The program ends when a successful conversion is made.

"""

# functions

def kmtomiles(km):
    return float(km)*0.621371
def milestokm(miles):
    return float(miles)*1.60934

def ctof(c):
    return float(c) * 9/5 + 32
def ftoc(f):
    return (float(fahrenheit)- 32) * 5/9

def kgtolb(kg):
    return float(kg) * 2.20462
def lbtokg(pound):
    return float(pound) * 0.453592

def sqmtosqft(sqmeter):
    return float(sqmeter) * 10.7639
def sqfttosqm(sqfoot):
    return float(sqfoot) / 10.7639

def usgallontolitre(usgallon):
    return float(usgallon) * 3.78541
def litretousgallon(litre):
    return float(litre) * 0.264172

def jouletogramcalorie(joule):
    return float(joule) * 0.239006
def gramcalorietojoule(gramcalorie):
    return float(gramcalorie) * 4.184


print("--- Unit Converter ---")

while True:
    print()
    menu_1 = input("Please type in the number of your corresponding conversion type: \n"
                   "1 - Distance \n"
                   "2 - Temperature \n"
                   "3 - Mass \n"
                   "4 - Area \n"
                   "5 - Volume \n"
                   "6 - Energy \n"
                   "7 - EXIT PROGRAM \n: ")
    print()

    if menu_1 == "1":
        while True:
            print()
            menu_2 = input("Please type in the number of your corresponding conversion order: \n"
                                    "1 - Kilometers to miles \n"
                                    "2 - Miles to kilometers \n"
                                    "3 - Exit to conversion type selection\n: ")
            if menu_2 == "1":
                km = input("Please input the number of kilometers you would like to convert into miles: ")
                print(f"{km} km in miles is about {kmtomiles(km)} miles.")
            elif menu_2 == "2":
                miles = input("Please input the number of miles you would like to convert into kilometers: ")
                print(f"{miles} miles in kilometers is about {milestokm(miles)} km.")
            elif menu_2 == "3":
                break
            else:
                print("Invalid input, please try again."),
                continue

    elif menu_1 == "2":
        while True:
            print()
            menu_2 = input("Please type in the number of your corresponding conversion order: \n"
                                    "1 - Celsius to Fahrenheit \n"
                                    "2 - Fahrenheit to Celsius \n"
                                    "3 - Exit to conversion type selection\n: ")
            if menu_2 == "1":
                celsius = input("Please input the temperature in Celsius you would like to convert into Fahrenheit: ")
                print(f"{celsius} degrees Celsius in Fahrenheit is about {ctof(celsius)} degrees Fahrenheit.")
            elif menu_2 == "2":
                fahrenheit = input("Please input the temperature in Fahrenheit you would like to convert into Celsius: ")
                print(f"{fahrenheit} degrees Fahrenheit in Celsius is about {ftoc(fahrenheit)} degrees Celsius.")
            elif menu_2 == "3":
                break
            else:
                print("Invalid input, please try again."),
                continue


    elif menu_1 == "3":
        while True:
            print()
            menu_2 = input("Please type in the number of your corresponding conversion order: \n"
                                    "1 - Kilogram to pound \n"
                                    "2 - Pound to kilogram \n"
                                    "3 - Exit to conversion type selection\n: ")
            if menu_2 == "1":
                kg = input("Please input the number of kilograms you would like to convert into pounds: ")
                print(f"{kg} kg in pounds is about {kgtolb(kg)} pounds.")
            elif menu_2 == "2":
                pound = input("Please input the number of pounds you would like to convert into kilograms: ")
                print(f"{pound} lb in kg is about {lbtokg(pound)} kg.")
            elif menu_2 == "3":
                break
            else:
                print("Invalid input, please try again."),
                continue



    elif menu_1 == "4":
        while True:
            print()
            menu_2 = input("Please type in the number of your corresponding conversion order: \n"
                                    "1 - Square meter to square foot \n"
                                    "2 - Square foot to square meter \n"
                                    "3 - Exit to conversion type selection\n: ")
            if menu_2 == "1":
                sqmeter = input("Please input the area in square meters you would like to convert into square foot: ")
                print(f"{sqmeter} m^2 in square foot is about {sqmtosqft(sqmeter)} ft^2.")
            elif menu_2 == "2":
                sqfoot = input("Please input the area in square meters you would like to convert into square foot: ")
                print(f"{sqfoot} ft^2 in square meter is about {sqfttosqm(sqfoot)} m^2.")
            elif menu_2 == "3":
                break
            else:
                print("Invalid input, please try again."),
                continue

    elif menu_1 == "5":
        while True:
            print()
            menu_2 = input("Please type in the number of your corresponding conversion order: \n"
                                    "1 - US gallon to litre \n"
                                    "2 - Litre to US gallon \n"
                                    "3 - Exit to conversion type selection\n: ")
            if menu_2 == "1":
                usgallon = input("Please input the volume in US gallons you would like to convert into litres: ")
                print(f"{usgallon} US gallon(s) in L is about {usgallontolitre(usgallon)} L.")
            elif menu_2 == "2":
                litres = input("Please input the volume in litres you would like to convert into gallons: ")
                print(f"{litres} L in gallon(s) is about {litretousgallon(litres)} gallon(s).")
            elif menu_2 == "3":
                break
            else:
                print("Invalid input, please try again."),
                continue



    elif menu_1 == "6":
        while True:
            print()
            menu_2 = input("Please type in the number of your corresponding conversion order: \n"
                                    "1 - Joule to gram calorie \n"
                                    "2 - Gram calorie to joule \n"
                                    "3 - Exit to conversion type selection\n: ")
            if menu_2 == "1":
                joule = input("Please input the energy in joules you would like to convert gram calories: ")
                print(f"{joule} gram calorie(s) is about {jouletogramcalorie(joule)} joule(s).")
            elif menu_2 == "2":
                gramcalorie = input("Please input the energy in gram calories you would like to convert into joules: ")
                print(f"{gramcalorie} gram calorie(s) is about {sqfttosqm(gramcalorie)} joule(s).")
            elif menu_2 == "3":
                break
            else:
                print("Invalid input, please try again."),
                continue

    elif menu_1 == "7":
        break



    else:
        print("Invalid input, please try again."),
        continue


"""
Project 3 v 1.1
"""
global_var = ""


def length_choice():
    global global_var
    print()
    print("Press 1 to convert meters into inches.")
    print("Press 2 to convert inches into meters.")
    user_choice_1 = int(input("Input your choice: "))
    global_var = user_choice_1


def temperature_choice():
    global global_var
    print()
    print("Press 1 to convert celsius into fahrenheit.")
    print("Press 2 to convert fahrenheit into celsius.")
    user_choice_1 = int(input("Input your choice: "))
    global_var = user_choice_1


def weight_choice():
    global global_var
    print()
    print("Press 1 to convert kg into pounds.")
    print("Press 2 to convert pounds into kg.")
    user_choice_1 = int(input("Input your choice: "))
    global_var = user_choice_1


def area_choice():
    global global_var
    print()
    print("Press 1 to convert square meters into acres.")
    print("Press 2 to convert acres into square meters.")
    user_choice_1 = int(input("Input your choice: "))
    global_var = user_choice_1


def water_volume_choice():
    global global_var
    print()
    print("Press 1 to convert gallons into liters.")
    print("Press 2 to convert liters into gallons.")
    user_choice_1 = int(input("Input your choice: "))
    global_var = user_choice_1


def length_converter():
    print()
    user_input_num = float(input("Please enter the quantity of this item to convert: "))
    if global_var == 1:
        print(f"If you convert {user_input_num} meters into inches you get {user_input_num * 39.37} inches.")
    elif global_var == 2:
        print(f"If you convert {user_input_num} inches into meter you get {user_input_num / 39.37} meters.")


def temperature_converter():
    print()
    user_input_num = float(input("Please enter the quantity of this item to convert: "))
    if global_var == 1:
        print(
            f"If you convert {user_input_num} celsius into fahrenheit you get {user_input_num * 1.8 + 32} fahrenheit.")
    elif global_var == 2:
        print(
            f"If you convert {user_input_num} fahrenheit into celsius you get {(user_input_num - 32) * (5 / 9)} celsius.")


def weight_converter():
    print()
    user_input_num = float(input("Please enter the quantity of this item to convert: "))
    if global_var == 1:
        print(f"If you convert {user_input_num} kg into pounds you get {user_input_num * 2.205} pounds.")
    elif global_var == 2:
        print(f"If you convert {user_input_num} pounds into kg you get {user_input_num / 2.205} kg.")


def area_converter():
    print()
    user_input_num = float(input("Please enter the quantity of this item to convert: "))
    if global_var == 1:
        print(f"If you convert {user_input_num} square meters into acres you get {user_input_num / 4047} acres.")
    elif global_var == 2:
        print(
            f"If you convert {user_input_num} acres into square meters you get {user_input_num * 4047} square meters.")


def water_volume_converter():
    print()
    user_input_num = float(input("Please enter the quantity of this item to convert: "))
    if global_var == 1:
        print(f"If you convert {user_input_num} gallons into liters you get {user_input_num * 4.546} liters.")
    elif global_var == 2:
        print(f"If you convert {user_input_num} liters into square gallons you get {user_input_num / 4.546} gallons.")


print("==Converter==")
print("Press 1 to use length converter.")
print("Press 2 to use temperature converter.")
print("Press 3 to use weight converter.")
print("Press 4 to use area converter.")
print("Press 5 to use water volume converter.")
user_input = int(input("Please input the number: "))

if user_input == 1:
    length_choice()
    length_converter()
elif user_input == 2:
    temperature_choice()
    temperature_converter()
elif user_input == 3:
    weight_choice()
    weight_converter()
elif user_input == 4:
    area_choice()
    area_converter()
elif user_input == 5:
    water_volume_choice()
    water_volume_converter()

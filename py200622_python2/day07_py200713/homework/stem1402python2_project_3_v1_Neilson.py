"""
Project 3
"""


def length_converter():
    starting_meter_length = float(input("Please input a number in meters: "))

    centimeter = starting_meter_length * 100
    decimeter = starting_meter_length * 10
    yard = starting_meter_length * 1.094
    inch = starting_meter_length * 39.37
    foot = starting_meter_length * 3.281
    length_list = [centimeter, decimeter, yard, inch, foot]
    length_list_2 = ["centimeter", "decimeter", "yard", "inch", "foot"]

    print("Press 1 to convert into centimeters")
    print("Press 2 to convert into decimeters")
    print("Press 3 to convert into yards")
    print("Press 4 to convert into inches")
    print("Press 5 to convert into feet")
    the_converter_type = int(input("Please enter the number: "))
    print(f"The conversion from kg to {length_list_2[the_converter_type - 1]} is "
          f"{length_list[the_converter_type - 1]}.")


def temperature_converter():
    starting_celsius_temperature = int(input("Please enter a number in celsius: "))
    fahrenheit = (starting_celsius_temperature + 9 / 5) + 32
    kelvin = starting_celsius_temperature + 273.15
    temperature_list = [fahrenheit, kelvin]
    temperature_list_2 = ["fahrenheit", "kelvin"]

    print("Press 1 to convert into fahrenheit.")
    print("Press 2 to convert into kelvin")
    the_converter_type = int(input("Please enter a number: "))
    print(f"The conversion from kg to {temperature_list_2[the_converter_type - 1]} is "
          f"{temperature_list[the_converter_type - 1]}.")


def weight_converter():
    starting_kg_weight = float(input("Please input a number in kg: "))

    pounds = starting_kg_weight * 2.205
    grams = starting_kg_weight * 1000
    ounces = starting_kg_weight * 35.274
    tonne = starting_kg_weight / 1000
    weight_list = [pounds, grams, ounces, tonne]
    weight_list_2 = ["pounds", "grams", "ounces", "tonne"]

    print("Press 1 to convert into pounds")
    print("Press 2 to convert into grams")
    print("Press 3 to convert into ounces")
    print("Press 4 to convert into tonne")
    the_converter_type = int(input("Please enter the number: "))

    print(f"The conversion from kg to {weight_list_2[the_converter_type - 1]} is "
          f"{weight_list[the_converter_type - 1]}.")


print("==Converter==")
print("Press 1 to use length converter.")
print("Press 2 to use temperature converter.")
print("Press 3 to use temperature converter.")
user_input = int(input("Please input the number: "))

if user_input == 1:
    length_converter()
elif user_input == 2:
    temperature_converter()
elif user_input == 3:
    weight_converter()






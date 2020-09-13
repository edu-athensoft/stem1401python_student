"""
dictionary
about the keys
"""

dict1 = {
    1: "value1",
    2: "value2",
    3: "value3",
    # ...
    1000: "value1000"
}

dict2_en = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday"
}

dict2_fr = {
    "mon": "Lundi",
    "tue": "Mardi",
    "wed": "Wednesday-fr",
    "thu": "Thursday-fr",
    "fri": "Friday-fr",
    "sat": "Saturday-fr",
    "sun": "Sunday-fr"
}

# how to find out the french version for the identical key
# zihan
for i in dict2_en:
    print(dict2_fr[i])

for key in dict2_en:
    print(dict2_en[key])
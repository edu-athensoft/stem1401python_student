"""
string to datetime object
"""

from datetime import datetime

date_string = "6 December, 2020  01:10:38"

print("date_string =", date_string)
print("type of date_string =", type(date_string))


try:
    date_object = datetime.strptime(date_string, "%d %B, %Y  %H:%M:%S")

except ValueError as ve:
    print("String does not match!")

print("date_object =", date_object)
print("type of date_object =", type(date_object))
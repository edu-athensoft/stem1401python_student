"""
date object to represent a date

constructor - a special function of a class
"""

# specify a date and create a date object

from datetime import date

year = 2020
month = 11
day = 15

date_obj = date(year, month, day)
print(date_obj, type(date_obj))

# users may input by themselves from keyboard

date_obj = date(2020, 11, 15)
print(date_obj, type(date_obj))
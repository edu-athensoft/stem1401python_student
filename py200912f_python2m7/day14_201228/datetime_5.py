"""
print today's year, month and day

"""

from datetime import date

# get today

td = date.today()
print(td, type(td))


# get year
y = td.year
print("Year: ", y)

# get month
m = td.month
print("Month: ", m)

# get day
d = td.day
print("Day: ", d)

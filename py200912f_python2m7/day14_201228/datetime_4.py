"""
to create a date object
"""

import datetime

# create date object for today
d = datetime.date(2020,12,28)
print(d, type(d))


# create date object for a specific day

d2 = datetime.date(2021,1,1)
print(d2, type(d2))

#
d3 = datetime.date(1900,1,1)
print(d3, type(d3))


# create a date from a timestamp
# 1970.1.1 0:0:0  epoch date and time

timestamp = datetime.date.fromtimestamp(1609201234)
print("date = ", timestamp)




"""

get timestamp from a datetime object
datetime.timestamp()
"""

from datetime import datetime
a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)

# get timestamp
print("timestamp =", a.timestamp())


# ex. write a program to get current datetime's timestamp

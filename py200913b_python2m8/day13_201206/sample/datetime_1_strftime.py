"""
datetime to string using strftime()
"""

from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

month = now.strftime("%B")
print("month:", month)

month = now.strftime("%b")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

date_time = now.strftime("%Y-%b-%d, %H:%M:%S")
print("date and time:",date_time)
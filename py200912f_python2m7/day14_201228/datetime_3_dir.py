"""
list classes in datetime
"""

import datetime

# dir() - list all property and functions in a module

result = dir(datetime)

for item in result:
    print(item)


print(datetime.MAXYEAR, datetime.MINYEAR)
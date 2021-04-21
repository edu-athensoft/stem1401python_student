"""
python date and time

modules:
1. datetime
1.1 datetime
1.2 date
1.3 time
1.4 timedelta
1.5 timezone

"""


# ex 1.  get current date and time

import datetime

datetime_obj = datetime.datetime.now()

print(datetime_obj, type(datetime_obj))


# ex 2. get current date
date_obj = datetime.date.today()

print(date_obj, type(date_obj))
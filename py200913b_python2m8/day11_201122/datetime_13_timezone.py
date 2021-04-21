"""
list all time zones

module: pytz

timezone:
1. continent/city name
Canada/Eastern
America/Montreal
2.CET
3.Etc
Etc/Universal
Etc/UTC
Etc/Greenwich
Etc/GMT0

pip

"""

from pytz import all_timezones

len_of_timezone = len(all_timezones)
print(len_of_timezone)

for tz in all_timezones:
    print(tz)


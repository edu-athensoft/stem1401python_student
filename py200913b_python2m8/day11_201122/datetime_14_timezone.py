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

GMT
UTC

Canada/Eastern
America/Toronto
"""

from pytz import common_timezones

len_of_timezone = len(common_timezones)
print(len_of_timezone)

for tz in common_timezones:
    print(tz)


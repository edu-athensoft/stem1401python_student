"""
get date form a timestamp

1970-01-01 at UTC

"""

from datetime import date

# OSError
timestamp = date.fromtimestamp(1590458943)
print(type(timestamp))
print("date=", timestamp)


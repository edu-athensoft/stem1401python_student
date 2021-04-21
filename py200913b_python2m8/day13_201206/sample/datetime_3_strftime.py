"""
Locale's appropriate date and time

Format codes %c, %x and %X are used for locale's appropriate date and time representation.
"""


from datetime import datetime

now = datetime.now()

timestamp = now.timestamp()
date_time = datetime.fromtimestamp(timestamp)

d = date_time.strftime("%c")
print("Output 1:", d)

d = date_time.strftime("%x")
print("Output 2:", d)

d = date_time.strftime("%X")
print("Output 3:", d)
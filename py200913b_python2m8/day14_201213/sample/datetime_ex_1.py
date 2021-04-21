"""
date.today()
date.weekday()

"""


from datetime import date
from datetime import timedelta

today = date.today()
print(today.weekday())

offset = (today.weekday() - 1) % 7

last_tuesday = today - timedelta(days=offset)

print(last_tuesday)
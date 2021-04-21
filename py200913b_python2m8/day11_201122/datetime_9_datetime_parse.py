"""
datetime object

datetime.year
datetime.month
datetime.day
datetime.hour
"""


from datetime import datetime

dt1 = datetime(2020,11,15,12, 10, 35, 200321)
print(dt1)

dt2 = datetime.now()
print(dt2)

dt3 = datetime(2020,11,15)
print(dt3)


# parsing
print(f"year:{dt2.year}")
print(f"month:{dt2.month}")
print(f"day:{dt2.day}")
print(f"hour:{dt2.hour}")
print(f"min:{dt2.minute}")
print(f"second:{dt2.second}")
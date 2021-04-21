"""
get today's year, month and day

parsing

xml
<tag>xxxx</tag>

"""

from datetime import date

today_obj = date.today()
print(today_obj)
print()

print(f"year:{today_obj.year}")
print(f"year:{today_obj.month}")
print(f"year:{today_obj.day}")


# exercise
# parsing 2025-12-25

holiday= date(2025, 12, 25)
today_obj = holiday

print(f"year:{today_obj.year}")
print(f"year:{today_obj.month}")
print(f"year:{today_obj.day}")
print()

#
holiday= date(1, 12, 1)
print(today_obj)
today_obj = holiday

print(f"year:{today_obj.year}")
print(f"year:{today_obj.month}")
print(f"year:{today_obj.day}")
print()

print("=== default date===")
default_date = date(2020, 2, 4)
print(default_date)
# today_obj = default_date
#
# print(f"year:{today_obj.year}")
# print(f"year:{today_obj.month}")
# print(f"year:{today_obj.day}")
print()


#
year = int(input())
month = int(input())
day = int(input())

try:
    holiday= date(year, month, day)
    print(today_obj)
    today_obj = holiday

    print(f"year:{today_obj.year}")
    print(f"year:{today_obj.month}")
    print(f"year:{today_obj.day}")
    print()
except ValueError as ve:
    print(ve)
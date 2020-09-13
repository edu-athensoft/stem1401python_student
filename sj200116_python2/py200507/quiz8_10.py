"""
Author:  Yun Gong Zhang
"""

days = int(input("Please enter a number of days: "))
TODAY = int(input("Please input today's day: "))

daysleft = days % 7

rest = daysleft + TODAY

if rest == 1:
    print("It is a Monday.")
elif rest == 2:
    print("It is a Tuesday.")
elif rest == 3:
    print("It is a Wednesday.")
elif rest == 4:
    print("It is a Thursday.")
elif rest == 5:
    print("It is a Friday.")
elif rest == 6:
    print("It is a Saturday.")
else:
    print("It is a Sunday.")
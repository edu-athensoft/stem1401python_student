"""
Leap year

a given year number
to check if that year is a leap year

year = 1900
question: Is the year of 1900 a leap year?
366 days every 4 year

1. if the number of year can be perfectly divided by 4, year is probably a leap year.
2. if the number of year can be also per. divided by 100, that year is probably not a leap year.
3. if the number of year can be also per. divided by 400, that year is a leap year.

"""

year = 2100

if year % 4 == 0:
    # print("probably a leap year")
    if year % 100 == 0:
        # print("probably Not a leap year")
        if year % 400 ==0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))





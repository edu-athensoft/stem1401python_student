"""
test if the year is a leap year
"""

# input the year
year = int(input("Please enter a year:"))

# perform checking
if year % 100 == 0:
    if year % 400 == 0:
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))

elif year % 4 == 0:
    if year % 100 == 0:
        print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))

elif year % 400 == 0:
    print("{} is not a leap year".format(year))



# if True:
#     pass
#
# if True:
#     pass
#
# if True:
#     pass
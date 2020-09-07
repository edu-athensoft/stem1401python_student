"""
ex3.
write a program to check leap year

1900
2020
2000
2019
"""

"""
# lucas
year = int(input("Enter year to be checked: "))
strtemp1 = "{} is a leap year".format(year)
strtemp2 = "{} is not a leap year".format(year)
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print(strtemp1.format(year))
        else:
            print(strtemp2.format(year))
    else:
        print(strtemp1.format(year))
else:
    print(strtemp2.format(year))
"""


# xuanxuan
year_num = int(input('Input a year number: '))
if year_num % 400 == 0:
    print('{} is a leap year.'.format(year_num))
elif year_num % 100 == 0:
    print('{} is not a leap year.'.format(year_num))
elif year_num % 4 == 0:
    print('{} is a leap year.'.format(year_num))
else:
    print('{} is not a leap year.'.format(year_num))


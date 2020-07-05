"""
If a year is a leap year
"""
print('Check if it is a leap year')
print()

in_year = int(input("Please enter the year: "))

if in_year < 0:
    print("That is not a valid year")
elif in_year % 4 == 0:
    if in_year % 100 == 0:
        if in_year % 400 == 0:
            print("That is a leap year")
        else:
            print("That is not a leap year")
    else:
        print("That is a leap year")
else:
    print("That is not a leap year")
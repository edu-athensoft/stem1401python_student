

print("This program tell you if this year is or is not a leap year")

a = int(input("Please enter a year: "))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("This year is a leap year.")
        else:
            print("This year isn't a leap year.")
    else:
        print("This year is a leap year.")
else:
    print("This year isn't a leap year.")






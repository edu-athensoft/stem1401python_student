"""
Leap year checker.
"""
print("Leap year checker.")

print()

year = int(input("Input year: "))


# if year is not divisible by 4, not a leap year.
if year%4 != 0:
    print("It is not a leap year.")
# elif year is not divisible by 100, leap year.
elif year%100 != 0:
    print("It is a leap year.")
# elif year is divisible by 400, leap year.
elif year%400 == 0:
    print("It is a leap year.")
# else (year is divisible by 100 but not 400), not a leap year.
else:
    print("It is not a leap year.")
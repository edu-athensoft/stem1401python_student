"""
Quiz 8
"""

# Question 8

if "a" in "alphabet":
    print("There is an a in alphabet")
else:
    print("There is not an a in alphabet")
print()

# Question 9

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]

if list_1 == list_2:
    print("Both lists have the same items")
else:
    print("The lists don't have same items")

print()
# Question 10
Days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
Days_Value = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

print("100 days from now")

entered_day = input("Please enter a day of the week with only the first letter in capitals: ")
remainder = 100 % 7

if entered_day == Days_of_the_week[0]:
    The_100_day = Days_Value["Monday"] + remainder
    if The_100_day == 1:
        print("The 100th day from Monday is Monday.")
    elif The_100_day == 2:
        print("The 100th day from Monday is Tuesday.")
    elif The_100_day == 3:
        print("The 100th day from Monday is Wednesday.")
    elif The_100_day == 4:
        print("The 100th day from Monday is Thursday.")
    elif The_100_day == 5:
        print("The 100th day from Monday is Friday.")
    elif The_100_day == 6:
        print("The 100th day from Monday is Saturday.")
    else:
        print("The 100th day from Monday is Sunday.")

elif entered_day == Days_of_the_week[1]:
    The_100_day = Days_Value["Tuesday"] + remainder
    if The_100_day == 1:
        print("The 100th day from Tuesday is Monday.")
    elif The_100_day == 2:
        print("The 100th day from Tuesday is Tuesday.")
    elif The_100_day == 3:
        print("The 100th day from Tuesday is Wednesday.")
    elif The_100_day == 4:
        print("The 100th day from Tuesday is Thursday.")
    elif The_100_day == 5:
        print("The 100th day from Tuesday is Friday.")
    elif The_100_day == 6:
        print("The 100th day from Tuesday is Saturday.")
    else:
        print("The 100th day from Tuesday is Sunday.")

elif entered_day == Days_of_the_week[2]:
    The_100_day = Days_Value["Wednesday"] + remainder
    if The_100_day == 1:
        print("The 100th day from Wednesday is Monday.")
    elif The_100_day == 2:
        print("The 100th day from Wednesday is Tuesday.")
    elif The_100_day == 3:
        print("The 100th day from Wednesday is Wednesday.")
    elif The_100_day == 4:
        print("The 100th day from Wednesday is Thursday.")
    elif The_100_day == 5:
        print("The 100th day from Wednesday is Friday.")
    elif The_100_day == 6:
        print("The 100th day from Wednesday is Saturday.")
    else:
        print("The 100th day from Wednesday is Sunday.")

elif entered_day == Days_of_the_week[3]:
    The_100_day = Days_Value["Thursday"] + remainder
    if The_100_day == 1:
        print("The 100th day from Thursday is Monday.")
    elif The_100_day == 2:
        print("The 100th day from Thursday is Tuesday.")
    elif The_100_day == 3:
        print("The 100th day from Thursday is Wednesday.")
    elif The_100_day == 4:
        print("The 100th day from Thursday is Thursday.")
    elif The_100_day == 5:
        print("The 100th day from Thursday is Friday.")
    elif The_100_day == 6:
        print("The 100th day from Thursday is Saturday.")
    else:
        print("The 100th day from Thursday is Sunday.")

elif entered_day == Days_of_the_week[4]:
    The_100_day = Days_Value["Friday"] + remainder
    if The_100_day == 1:
        print("The 100th day from Friday is Monday.")
    elif The_100_day == 2:
        print("The 100th day from Friday is Tuesday.")
    elif The_100_day == 3:
        print("The 100th day from Friday is Wednesday.")
    elif The_100_day == 4:
        print("The 100th day from Friday is Thursday.")
    elif The_100_day == 5:
        print("The 100th day from Friday is Friday.")
    elif The_100_day == 6:
        print("The 100th day from Friday is Saturday.")
    else:
        print("The 100th day from Friday is Sunday.")

elif entered_day == Days_of_the_week[5]:
    The_100_day = Days_Value["Saturday"] + remainder
    if The_100_day == 8:
        print("The 100th day from Saturday is Monday.")
    elif The_100_day == 2:
        print("The 100th day from Saturday is Tuesday.")
    elif The_100_day == 3:
        print("The 100th day from Saturday is Wednesday.")
    elif The_100_day == 4:
        print("The 100th day from Saturday is Thursday.")
    elif The_100_day == 5:
        print("The 100th day from Saturday is Friday.")
    elif The_100_day == 6:
        print("The 100th day from Saturday is Saturday.")
    else:
        print("The 100th day from Saturday is Sunday.")

elif entered_day == Days_of_the_week[6]:
    The_100_day = Days_Value["Sunday"] + remainder
    if The_100_day == 8:
        print("The 100th day from Sunday is Monday.")
    elif The_100_day == 9:
        print("The 100th day from Sunday is Tuesday.")
    elif The_100_day == 3:
        print("The 100th day from Sunday is Wednesday.")
    elif The_100_day == 4:
        print("The 100th day from Sunday is Thursday.")
    elif The_100_day == 5:
        print("The 100th day from Sunday is Friday.")
    elif The_100_day == 6:
        print("The 100th day from Sunday is Saturday.")
    else:
        print("The 100th day from Sunday is Sunday.")

elif entered_day not in Days_of_the_week:
    print("Not a valid day.")

else:
    pass



"""
For May 22nd, 2020.
Quiz 8.
"""

# Question 8.
sentence = 'abc'

if 'a' in sentence or 'A' in sentence:
    print(True)
else:
    print(False)

print()

# Question 9.

list1 = [1, 2, "a"]
list2 = [1, 2, "a"]

print(list1 == list2)

print()

# Question 10.

print("Day of the week in the future calculator.")

# List of days of the week for future use of index
list_days_of_the_week = ["Monday",
                         "Tuesday",
                         "Wednesday",
                         "Thursday",
                         "Friday",
                         "Saturday",
                         "Sunday"]

# Remove case sensitivity
day_of_the_week = input("Please input the day of the week: ").lower().capitalize()

# Check for if spelling of day of the week is right
valid_day = False
for day in list_days_of_the_week:
    if day == day_of_the_week:
        valid_day = True
if not valid_day:
    print("Unrecognized day of the week. Please retry.")
    quit()


days_to = int(input("Please input how many days to the second date: "))

# Use of modulo to find index of future day.
index_day = list_days_of_the_week.index(day_of_the_week)
index_future_day = (index_day + days_to) % 7

print("In {} days, it will be a {}.".format(days_to, list_days_of_the_week[index_future_day]))




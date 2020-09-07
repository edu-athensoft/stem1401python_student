"""
dictionary

accessing items from a dictionary
"""


days_of_the_week = {
    'MON': 'Monday',
    'TUE': 'Tuesday',
    'WED': 'Wednesday',
    'THU': 'Thursday',
    'FRI': 'Friday',
    'SAT': 'Saturday',
    'SUN': 'Sunday'
}


# option 1. []
day = days_of_the_week['MON']
print(day)

# day = days_of_the_week['XYZ']       # error
# print(day)

# option 2. get()
day = days_of_the_week.get('TUE')
print(day)

day = days_of_the_week.get('XYZ')
print(day)

# get() v.s []



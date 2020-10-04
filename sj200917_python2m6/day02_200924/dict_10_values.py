"""
dictionary values()

dict.values()

"""

daysdict = {
    'MON': 'Monday',
    'TUE': 'Tuesday',
    'WED': 'Wednesday',
    'THU': 'Thursday',
    'FRI': 'Friday',
    'SAT': 'Saturday',
    'SUN': 'Sunday',
    'OTH': 'Sunday'
}

print(daysdict.values())
print(type(daysdict.values()))

# list()
allvalues = list(daysdict.values())
print(allvalues, type(allvalues))

# iterable
for value in allvalues:
    print(value, type(value))

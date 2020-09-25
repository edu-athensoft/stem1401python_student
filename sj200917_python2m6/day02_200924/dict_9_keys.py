"""
dictionary
keys()

dict.keys()

"""

daysdict = {
    'MON': 'Monday',
    'TUE': 'Tuesday',
    'WED': 'Wednesday',
    'THU': 'Thursday',
    'FRI': 'Friday',
    'SAT': 'Saturday',
    'SUN': 'Sunday'
}

print(daysdict.keys())
print(type(daysdict.keys()))

# list()
allkeys = list(daysdict.keys())
print(allkeys, type(allkeys))

# iterable
for key in allkeys:
    print(key, type(key))






"""
dictionary

remove items from dictionary

pop() - remove a particular item
popitem() - can be used to remove and return an arbitrary (key, value)
clear()
del -  remove individual items or the entire dictionary itself

"""
# pop()
days_of_the_week = {
    'MON': 'Monday',
    'TUE': 'Tuesday',
    'WED': 'Wednesday',
    'THU': 'Thursday',
    'FRI': 'Friday',
    'SAT': 'Saturday',
    'SUN': 'Sunday'
}

print(days_of_the_week.pop('SAT'))
print(days_of_the_week)

print(days_of_the_week.pop('SUN'))
print(days_of_the_week)
print()

# popitem()
days_of_the_week = {
    'MON': 'Monday',
    'TUE': 'Tuesday',
    'WED': 'Wednesday',
    'THU': 'Thursday',
    'FRI': 'Friday',
    'SAT': 'Saturday',
    'SUN': 'Sunday'
}
print(days_of_the_week.popitem())
print(days_of_the_week)
print()

# del
del days_of_the_week['MON']
print(days_of_the_week)
print()


# clear
days_of_the_week.clear()
print(days_of_the_week)
print()

del days_of_the_week
# print(days_of_the_week)
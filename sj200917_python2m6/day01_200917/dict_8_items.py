"""
dictionary
items()

item = (key, value)
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

"""
result = days_of_the_week.items()
print(result,type(result))

result = list(result)
print(result)

for item in result:
    # print(item, type(item))
    print(f'key={item[0]}, value={item[1]}')
"""
    
#
for item in days_of_the_week.items():
    print(item)

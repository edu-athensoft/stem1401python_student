"""
dictionary removing elements from a dictionary

pop() - removes an item with the provided key and returns the value
popitem() - can be used to remove and return an arbitrary (key, value) pair
clear() - remove all items
"""

months = {'Jan': 'January',
          'Feb': 'February',
          'Mar': 'March',
          'Apr': 'April',
          'May': 'May',
          'Jun': 'June',
          'Jul': 'July',
          'Aug': 'August',
          'Sep': 'September',
          'Oct': 'October',
          'Nov': 'November',
          'Dec': 'December'}

# pop()
value = months.pop("Dec")
print(value)
print(months)


# popitem()
item = months.popitem()
print(item, type(item))

# clear()
months.clear()
print(months)

months = {'Jan': 'January',
          'Feb': 'February',
          'Mar': 'March',
          'Apr': 'April',
          'May': 'May',
          'Jun': 'June',
          'Jul': 'July',
          'Aug': 'August',
          'Sep': 'September',
          'Oct': 'October',
          'Nov': 'November',
          'Dec': 'December'}

# del  keywords
# del key,value  (item)
# del dict
del months['Oct']
print(months)

del months
# print(months)
# NameError



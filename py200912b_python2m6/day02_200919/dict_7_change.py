"""
change or add element in a dictionary

if the key exists in the dictionary, then it performs updating value;
if the key does not exist, then it performs adding elements (key-value)
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


# case 1.
# change January -> in French Janvier
months['Jan'] = 'Janvier'
print(months)

# ex. change Februray -> in French


# case 2.
months['Unknown'] = 'Unknown-month'
print(months)


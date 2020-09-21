"""
Homework 1
"""

# 1.
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

# 2.
for i in months:
    print(months[i])


# 3.
user_profiles = {
    '1': {'userid': '1',
          'username': 'hello',
          'password': '12345678',
          'join_date': '01/01/2017'},
    '2': {'userid': '2',
          'username': 'sssssss',
          'password': 'sssssss',
          'join_date': '12/04/2015'},
    '3': {'userid': '3',
          'username': 'asdfasdfasdf',
          'password': 'qwertyuiop',
          'join_date': '06/09/2020'},
    '4': {'userid': '4',
          'username': 'goodbye',
          'password': '123123123',
          'join_date': '28/03/2017'}
}

# 4.
user1 = user_profiles['1']
print(user1)
print(user1['username'])
print(user1['password'])


for entry_key in user_profiles:
    print(entry_key, user_profiles[entry_key])


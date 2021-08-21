"""
[Homework]
Write programs for project 1 v2, and v3
Date: 2021-08-12
Due date: 2021-08-15
"""

# v2
user_name = input("Please input your username:")
password = input('Please input your password:')
if user_name == 'Admin' and password == 'whoknows':
    print('Welcome, {}! Your password is {}'.format(user_name, password))
else:
    print('Wrong username or password, please try it again')

print('=====v2 end here=====')

# v3
start = 1
end = 6
login_times = 0
for i in range(start, end):
    user_name = input("Please input your username:")
    password = input('Please input your password:')
    if user_name == 'Admin' and password == 'whoknows':
        print('Welcome, {}! Your password is {}'.format(user_name, password))
        break
    else:
        login_times += 1
        if login_times < 5:
            print('Wrong username or password, please try it again')
        if login_times == 5:
            print('Sorry, your account has been locked for security reasons, '
                  'if you want to continue logging in, please contact the manual customer service to unblock it.')
print('=====done=====')
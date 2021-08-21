"""
System analysis

multiple times of authenticating (login)
counting/limited times of authenticating

divide big problem into small problems or sub-problem

1. sub-problem.   unlimited times of authenticating
user can login unlimited times till they are correctly input.

2. sub-problem.   set constraints
counting when user finished login for once (increasing by 1)
if attemps reach max number of times (5), system displays failure information.
'User account Locked'
2.1 counting
2.2 max


3. Test case
3.1 correct at 1st
3.2 input less than 5 times
    incl. one success
3.3 input for 5 times
    no success

3.4 flexibility,generic
"""


# settings
# admin credentials
admin_username = 'Admin'
admin_password = 'whoknows'

MAX_ATTEMPS = 3

# application title
app_title = '=== My Login Form ver 3.0 ==='
print(app_title)

app_admin = 'for Administrators'
print(app_admin)
print()

app_attempts = 'You have 3 times of attempts.'
print(app_attempts)
print()

# counter for attempts
attemps = 0

while True:
    # input
    username = input("Please input your username:")
    password = input('Please input your password:')
    print()

    # record attempts
    attemps += 1
    print(f'You have tried for {attemps} time(s)')

    # authentication
    if username == admin_username and password == admin_password:
        print('Welcome, {}! Your password is {}'.format(username, password))
        print("You may use your personal center now!")
        break
    else:
        print('Wrong username or password!')
    print()

    # limited attempts
    if attemps >= MAX_ATTEMPS:
        print("Your account has been locked for security reason.")
        break

# output
print("Bye!")

"""
You were asked t o develop a text-based interactive application for your client.
The login program you wrote is functioning.

text-based - not GUI
interactive

system scope

settings
username = 'Admin'
password = 'whoknows'

Authentication - credential
Authorization  - privilege

case 1. input both correctly
case 2. input username correctly only
case 3. input password correctly only
case 4. input both incorrectly

"""

# settings
# admin credentials
admin_username = 'Admin'
admin_password = 'whoknows'


# application title
app_title = '=== My Login Form ver 2.0 ==='
print(app_title)

app_admin = 'for Administrators'
print(app_admin)
print()

# input
username = input("Please input your username:")
password = input('Please input your password:')
print()

# authentication
if username == admin_username and password == admin_password:
    print('Welcome, {}! Your password is {}'.format(username, password))
else:
    print('Wrong username or password, please try it again')

# output
print("You may use your personal center now!")

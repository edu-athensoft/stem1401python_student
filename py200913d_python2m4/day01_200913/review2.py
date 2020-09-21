"""
while-loop

Login form
It enables user to input the username and password for unlimited times till the user
correctly input the credentials

idea:
user input action is repeatable

if user input wrong username and password, then the user is asked to re-input

the times of input (loop) cannot be determined.

therefore, we have to use while-loop

"""

# correct credentials
expected_username = 'admin'
expected_password = '123'

# input
username = input("Please input your username:")
password = input("Please input your password:")

# check the input
"""
if username == expected_username and password == expected_password :
    print("Welcome back to the system, {}!".format(username))
else:
    print("Please try it again!")
"""

ispassed = username == expected_username and password == expected_password
while not ispassed:
    print("Please try it again!")
    username = input("Please input your username:")
    password = input("Please input your password:")
    ispassed = username == expected_username and password == expected_password

else:
    print("Welcome back to the system, {}!".format(username))











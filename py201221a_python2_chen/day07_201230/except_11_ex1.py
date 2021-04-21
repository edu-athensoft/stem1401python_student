"""
How to improve the login form program

v4.0

description:

No matter what users input, the program will not get crush.

users can input their username(s)
users can input their password

step 1. write normal programs

step 2. add try...except structure to make it more secure

"""


USERNAME = 'admin'
PWD = '123'

try:
    username = input('Please input your username: ')
    password = input('Please input your password: ')

except ValueError as ve:
    print(ve)
    print("Value Error occurred")

except TypeError as te:
    print(te)
    print("Type Error occurred")

except Exception:
    print("Internal Error!")


if username == USERNAME and password == PWD :
    print(f"Welcome {username}!")
else:
    print(f"Access denied.")










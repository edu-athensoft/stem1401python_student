"""
project: my password
version: 1
author: Ze Yue Li
date:

description: Setting Password
Please input a password from a keyboard, and the rules are as following:
1. at least 8 characters
2. Capital letter must be included
3. One or more letters must be included
3. One or more numbers must be included
4. One or more symbols must be included (valid symbols are only _, -, $, &, #, @, ! )
The program should allow users to try for unlimited times unless they type 'q' or 'quit'



"""

PWD_MIN_LEN = 8

password = ''
password_correct = False

while not password_correct:
    # flag of hasNumber, has number = 1, has not number = 0
    a = 0
    password = input('Please input a password:')
    if password == 'q' or password == 'quit':
        print('Program terminated')
        break
    if len(password) < PWD_MIN_LEN:
        print('Your password must be at least 8 characters long.')
        continue
    if password.lower() == password.upper():
        print('You need at least one letter.')
        continue
    if password.lower() == password:
        print('You need to have at least one capital letter.')
        continue
    for i in password:
        try:
            b = int(i)
            a = 1
        except ValueError:
            pass
    if a == 0:
        print('You need at least one digit.')
        continue
    if '_' not in password and '-' not in password and '$' not in password and '&' not in password and '#' not in password and '@' not in password and '!':
        print('You need at least one symbol.')
        continue
    password_correct = True
    print("Password accepted")
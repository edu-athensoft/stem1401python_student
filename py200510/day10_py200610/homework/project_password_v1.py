"""
project: my password
version: 1
author: Guang Zhu Cui
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

# program desc
print(
    'Hello, you must set a password now. The rules are: \n 1. at least 8 characters \n 2. Capital letter must be included \n '
    '3. One or more numbers must be included'
    '\n 4. One or more letters must be included'
    '\n 5. One or more symbols must be included (valid symbols are only _, -, $, &, #, @, ! )\n \n '
    'input "q" or "quit" if you want to quit.')
print()

# user input password
x = input('Please enter your password now:')


while True:
    while len(x) < 8 and x != 'q' and x != 'quit':
        print('Your password does not have at least 8 characters')
        x = input('Please enter a valid password:')

    while x.upper() in x and x.lower() in x and x != 'q' and x != 'quit':
        print('Your password does not contain a letter')
        x = input('Please enter a valid password:')
        continue

    while x.lower() == x and x != 'q' and x != 'quit':
        print('Your password does not contain a capital letter')
        x = input('Please enter a valid password:')

    while '0' not in x and '1' not in x and '2' not in x and '3' not in x and '4' not in x and '5' not in x and '6' not in x and '7' not in x and '8' not in x and '9' not in x and '0' not in x and x != 'q' and x != 'quit':
        print('Your password does not contain a number')
        x = input('Please enter a valid password:')

    while '_' not in x and '-' not in x and '$' not in x and '&' not in x and '#' not in x and '@' not in x and '!' not in x and x != 'q' and x != 'quit':
        print('Your password does not contain a symbol')
        x = input('Please enter a valid password:')

    if x == 'q' or x == 'quit':
        print('See you next time')
        break
    else:
        print('Your password is successfully set.')
        break

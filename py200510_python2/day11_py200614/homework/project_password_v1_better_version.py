"""
project: my password
version: 1.1
author: guang zhu cui
date:
"""
x = ''
print(
    'Hello, you must set a password now. The rules are: \n 1. at least 8 characters \n 2. Capital letter must be included \n '
    '3. One or more numbers must be included'
    '\n 4. One or more letters must be included'
    '\n 5. One or more symbols must be included (valid symbols are only _, -, $, &, #, @, ! )\n \n '
    'input "q" or "quit" if you want to quit.')
print()
def quit():
    if x == 'q' or 'quit':
        print('See you next time')
    else:
        return
def len_password():
    if len(x) <8:
       print('Your password does not have at least 8 characters')
    else:
        return
def letter_password():
    if x.upper() in x and x.lower() in x:
        print('Your password does not contain a letter')
    else:
        return
def capital_letter_password():
    if x.lower() == x:
        print('Your password does not contain a capital letter')
    else:
        return
def digit_password():
    if '0' not in x and '1' not in x and '2' not in x and '3' not in x and '4' not in x and '5' not in x and '6' not in x and '7' not in x and '8' not in x and '9' not in x:
        print('Your password does not contain a number')
def symbol_password():
    if '_' not in x and '-' not in x and '$' not in x and '&' not in x and '#' not in x and '@' not in x and '!' not in x:
        print('Your password does not contain a symbol')
    else:
        return
x = input('Please enter your password now:')
quit()
len_password()
letter_password()
capital_letter_password()
digit_password()
symbol_password()
print('succeed')





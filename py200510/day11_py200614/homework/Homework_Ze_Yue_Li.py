"""
project: my password
version: 1.1
author: ze yue li
date:
"""

password = ''
password_correct = False

def quit():
    if password == 'q' or password == 'quit':
        print("Program terminated")
        return True
    else:
        return False

def len_test():
    if len(password) < 8:
        print("Your password must be 8 characters long.")
        return True
    else:
        return False

def letter_test():
    if password.lower() == password.upper():
        print("You need at least one letter")
        return True
    else:
        return False

def cap_test():
    if password.lower() == password:
        print("You need at least one capital letter")
        return True
    else:
        return False

def num_test():
    a = 0
    b = 0
    for i in password:
        try:
            b = int(i)
            a = 1
        except ValueError:
            pass
    if a == 0:
        print('You need at least one digit.')
        return True
    else:
        return False

def sym_test():
    a = 0
    for i in password:
        try:
            int(i)
        except ValueError:
            password2.append(i)
    for i in password2:
        if i.lower() == i.upper():
            a = 1
    if a == 0:
        print("You need at least one symbol.")
        return True
    else:
        return False

while not password_correct:
    password2 = []
    password = input('Please input a password:')
    if quit():
        break
    if len_test():
        continue
    if letter_test():
        continue
    if cap_test():
        continue
    if num_test():
        continue
    if sym_test():
        continue
    password_correct = True
    print("Password accepted")

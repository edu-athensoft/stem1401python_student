"""
Guang Zhu Cui
2020/06/17
Password v2
v2. Generating Password
Please generate a password for your clients, the rules are as following:
1. at least 8 characters
2. Capital letter must be included
3. One or more letters must be included
3. One or more numbers must be included
4. One or more symbols must be included (valid symbols are only _, -, $, &, #, @, ! )
"""
import random
import string


# def Password():
def password():
    password_characters = string.ascii_uppercase + string.digits + '_-$&#@!' + string.ascii_lowercase
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice('_-$&#@!')
    for i in range(4):
        password += random.choice(password_characters)
    a = list(password)
    random.SystemRandom().shuffle(a)
    password = ''.join(a)
    return password


# print("Here is your password:", Password())
print("Here is your password:", password())

# test
print(string.ascii_uppercase)
print(string.digits)
print(string.ascii_lowercase)


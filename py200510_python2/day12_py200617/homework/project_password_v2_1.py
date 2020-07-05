"""
Guang Zhu Cui
2020/06/17
Password v2.1
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
def password(pwd_length):
    password_characters = string.ascii_uppercase + string.digits + '_-$&#@!' + string.ascii_lowercase
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice('_-$&#@!')

    #
    fixed_chars_len = 4
    for i in range(pwd_length - fixed_chars_len):
        password += random.choice(password_characters)
    a = list(password)
    random.SystemRandom().shuffle(a)
    password = ''.join(a)
    return password


# print("Here is your password:", Password())
PWD_LEN = 10
print("Here is your password:", password(PWD_LEN))

# test
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.ascii_lowercase)


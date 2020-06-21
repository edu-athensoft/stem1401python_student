"""
Ze Yue Li
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

cap_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
small_letters = list('abcdefghijklmnopqrstuvwxyz')
numbers = list('0123456789')
symbols = list('_-$&#@!')
all_chars = cap_letters + small_letters + numbers + symbols
password = ''

def add(added_list):
    return added_list[random.randint(0,len(added_list)-1)]

password += add(cap_letters)
password += add(small_letters)
password += add(numbers)
password += add(symbols)
while len(password) < 8:
    password += add(all_chars)

# print('Here is your password:', password)

print('Here is your password:', password)


pwd = list(password)
print(pwd)
random.shuffle(pwd)
print(pwd)
pwd = ''.join(pwd)

print('Here is your password:', pwd)




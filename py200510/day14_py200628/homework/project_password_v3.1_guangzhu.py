"""
Password v3
Guang Zhu Cui
2020-06-21
v3. Encrypting Password
For security reasons, the password should not directly be persisted into databases in original form.
It is recommended that every character should get right shifted for 3 steps.
For example,
a -> d,   b -> e,  c -> f,  …, 0 -> 3
print out the encrypted password
then decrypt the password and print it out to compare it with the original one
"""
def encrypted(password):
    for i in password:
        print(chr(ord(i) + 3))

def decrypted(decrypt_password):
    for i in decrypt_password:
        print(chr(ord(i) - 3))


# set a password for test
password = 'RETRE_BOSS1'
print('the password is:', password)

print('========= encrypted password ========')
encrypted(password)

print('========= decrypted password ========')
decrypt_password = 'UHWUHbERVV4'
decrypted(decrypt_password)



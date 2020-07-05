"""
Password v3.1
Ze Yue Li
2020-06-21
v3. Encrypting Password
For security reasons, the password should not directly be persisted into databases in original form.
It is recommended that every character should get right shifted for 3 steps.
For example,
a -> d,   b -> e,  c -> f,  …, 0 -> 3
print out the encrypted password
then decrypt the password and print it out to compare it with the original one
"""

def encrypt(password):
    encrypted_password = ''
    for i in password:
        encrypted_password += characters[characters.index(i) + 3]
    return encrypted_password


def decrypt(password):
    decrypted_password = ''
    for i in password:
        decrypted_password += characters[characters.index(i, 3) - 3]
    return decrypted_password

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-$&#@!abc'
password = "A_b12$#nd"

print(password)

coded_password = encrypt(password)
print(coded_password)

decoded_password = decrypt(coded_password)
print(decoded_password)

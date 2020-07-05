"""
Password v3
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
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-$&#@!abc'
password = "A_b12$#nd"
encrypted_password = ''
decrypted_password = ''
# Encrypting
for i in password:
    encrypted_password += characters[characters.index(i) + 3]
# Decrypting
for i in encrypted_password:
    decrypted_password += characters[characters.index(i, 3) - 3]

print(password)
print(encrypted_password)
print(decrypted_password)

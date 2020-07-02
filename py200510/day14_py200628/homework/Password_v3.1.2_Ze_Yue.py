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
# Encrypt function

def encrypt(password):
    """

    :param password:
    :return:
    """
    encrypted_password = ''
    for i in password:
        encrypted_password += characters[characters.index(i) + encrypt_num]
    return encrypted_password

# Decrypt function
def decrypt(password):
    """

    :param password:
    :return:
    """
    decrypted_password = ''
    for i in password:
        decrypted_password += characters[characters.index(i, encrypt_num) - encrypt_num]
    return decrypted_password


# Main program
# Setup
# settings 1. valid characters
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-$&#@!abc'

# settings 2. shifting number for encrypting algorithm
encrypt_num = 3


# set a password for test
password = "A_b12$#nd"
print(password)

# encrypt the password
coded_password = encrypt(password)
print(coded_password)

# decrypt the password and print out
decoded_password = decrypt(coded_password)
print(decoded_password)


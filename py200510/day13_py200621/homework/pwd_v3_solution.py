"""
password
v3
encrypt
decrypt
"""


def encrypt(char):
    pass


def decrypt(ascii):
    pass



pwd =  'asdfsdfasdfas'
encrypt_pwd = []
decrypt_pwd = ""

for c in pwd:
    encrypt_pwd.append(encrypt(c))

print("encrypted pwd is:", encrypt_pwd)


for pc in encrypt_pwd:
    decrypt_pwd += decrypt(pc)

print("encrypted pwd is:", decrypt_pwd)



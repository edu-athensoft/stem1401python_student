"""
encrypting a password
decrypting a password
"""


char = '%'
print("original char :",char)

# encrypting
# get ascii number
asc_no = ord(char)
print(asc_no)
print()


asc_no += 3
en_char = chr(asc_no)
print("en_char :",en_char)

# decrypting
pwd_asc_no = ord(en_char)
print(pwd_asc_no)
print()


pwd_asc_no -= 3
de_char = chr(pwd_asc_no)
print("de_char :",de_char)



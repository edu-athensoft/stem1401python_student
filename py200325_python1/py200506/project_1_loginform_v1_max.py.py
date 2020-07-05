"""
loginform || Max Yang
"""


# correct username is: u
# correct password is: p

# if the username is right the first time
username1 = "u"
username = input("Enter your username: ")

if username == "u":
    print("Username: {}".format(username1))

# if the username is wrong the first time
while username != username1:
    unknown_username = input("Unknown username. Please try again: ")

    if unknown_username is username1:
        print("Username: {}".format(username1))
        break

    else:
        continue

# if the password is right the first time
u_password = "p"
password = input("Enter your password: ")

if password == u_password:
    print("Password: {}".format(password))
    print("Login successful")

# if the password is wrong the first time
while password != u_password:
    wrong_password = input("Wrong password. Please try again: ")

    if wrong_password is u_password:
        print("Password: {}".format(wrong_password))
        print("Login successful")
        break

    else:
        continue

print("Hello!")
message1 = input()
print("Goodbye!")
message2 = input()
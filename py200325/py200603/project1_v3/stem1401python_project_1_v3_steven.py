"""
project_1_v3_steven
"""

print("Hello")
print("This program will check your username and password for this site.")
print("-------------------------------------------------------------------")


counter = 0
while counter < 5:
    username = input("Please enter your username:")
    password = input("Please enter your password:")
    if username == "James":
        if password == "james":
            print("Welcome {}! Your password is {}.".format(username, password))
            break

    else:
        print("Sorry the username or password is incorrect, please try again.")
        print("-------------------------------------------------------------------")
    counter += 1

if counter == 5:
    print()
    print("Sorry, your account has been locked for security reasons.")
    print("Please try again later.")







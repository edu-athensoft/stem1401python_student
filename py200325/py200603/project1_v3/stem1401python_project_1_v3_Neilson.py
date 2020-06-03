"""
Login Form version 3
"""
num_of_tries = 5

print("Welcome to your Login-Form")

while num_of_tries != 0:
    username = input("Please enter your username: ")

    if username == "Neilson":
        password = input("Please enter your password: ")
        if password == "1qaz2wsx":
            print("Welcome back {} and your password is {}!".format(username, password))
            break
        else:
            num_of_tries -= 1
            if num_of_tries == 0:
                print("Sorry your account has been blocked for security reasons.")
            else:
                print("Sorry that is not the corresponding password to the username {}.".format(username))
                continue
    else:
        num_of_tries -= 1
        if num_of_tries == 0:
            print("Sorry your account has been blocked for security reasons.")
        else:
            print("Sorry that is not your username.")
            continue

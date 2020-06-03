"""
For June 3rd, 2020.
stem1401_python_login_form_v3_ken
Login Form version 3.
Kenneth Chen.
"""

# to-dos:
    # credentials storage system
    # input system: usernam+ password
    # authentication
    # success print
    # failure print
    # failure 5 times

# idea
    # 1. dictionary for credentials
    # 2. use infinite while loop to redo steps 3-5
        # 3. if password_errors + username_errors is bigger than 3, print error message with "try again later" reason and quit
        # 4. input username
        # 5. input password
        # 6. try to compare the entered password with value associated with username in dictionary
            # 7. if it can compare them but it's false, print error, +1 to password_errors and continue
                # 8. if password_errors is bigger than 4, print error message with "security of account" reason and quit
            # 9. if it can't because the username doesn't exist inside the dictionary, print error, +1 to username_errors and continue
        # 10. print with .format the welcome message and break the while loop

credentials = {
    "Peter" : "123",
    "Chris" : "Ga1",
    "Michael" : "uwu",
    "Steve" : "xdx10"
}
entered_username = None
entered_password = None
username_errors = 0
password_errors = 0

print("---Login form v3---")

while True:
    if password_errors + username_errors > 4:
        print("Too many errors. Please try again at a later time.")
        exit()
    entered_username = input("Please enter your username: ")
    entered_password = input("Please enter your password: ")
    try:
        if entered_password != credentials[entered_username]:
            password_errors += 1
            if password_errors > 4:
                print("Your account has been locked for security reasons.")
                exit()
            print("Wrong username or password, try again.")
            continue
    except KeyError:
        username_errors += 1
        print("Wrong username or password, try again.")
        continue
    print("Welcome {}! Your password is {}.".format(entered_username, entered_password))
    break
"""
project_1_loginform_v1_ken.py
Login Form.
"""

# Blank comments to separate the parts of the program.

# Dictionary keeping username and password data.
credentials = {
    "Athens" : "123",
    "Cheng" : "987",
    "Ken" : "qwe",
    "Kevin" : "64209",
    "Max" : "nby",
    "Steven" : "mmm"
}


# while loop : Restarts program when login fails.
while True:
    #
    print("--- Login Form --- \n")

    #
    username = input("Please input your username (case sensitive): ")

    """for loop : checks if at least one username from dictionary "credentials" corresponds with the one input by the user and if so
    changes valid_username from False to True"""
    valid_username = False

    for key_username in credentials:
        if username == key_username:
            valid_username = True
            # break to stop looking for username if found in order to save processing power.
            break
        else:
            pass
    # Username input failure.
    if valid_username == False:
        print("Username does not exist!")
        username_fail_restart_quit = input("Input q to quit or anything else to try again: ")
        # Allowed inputs q and Q to remove case sensitivity.
        if username_fail_restart_quit == "q" or username_fail_restart_quit == "Q":
            print("You have exited the program!")
            exit()
    else:
        #
        password = input("Please input your password (case sensitive): ")


        # This checks if the credentials (username and password association) are correct.
        if credentials[username] == password:
            # break to leave while loop
            break
        # Credentials don't work failure.
        else:
            print("Invalid username or password!")
            password_fail_restart_quit = input("Input q to quit or anything else to try again: ")
            # Allowed inputs q and Q to remove case sensitivity.
            if password_fail_restart_quit == "q" or password_fail_restart_quit == "Q":
                print("You have exited the program!")
                exit()
                # break     # modified by Athens on 2020-05-06
            else:
                pass


# Use of placeholder {} as username and password in the following string.
print("Your username is «{}» and your password is «{}». Hello! :D".format(username, password))

#
print("Goodbye!")


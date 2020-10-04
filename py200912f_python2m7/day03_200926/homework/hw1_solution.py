"""
step 1. username
    expect the boolean result of checking username if it is valid or not
    case 1. one-word username
    case 2. multiple-word username

    if user input a valid username, program goes on
    else an error should be raised.

step 2. password

"""

class UserNameError(ValueError):
    pass



"""
# case 1.
def isvalid_username(username):
    return username.isalpha()

# test
print(isvalid_username('issa'))
print(isvalid_username('issa2'))
print()
"""

# case 2.
def isvalid_username(username):
    words = username.split()
    for word in words:
        if not word.isalpha():
            return False
    return True


# test 2
# print(isvalid_username("abc deg"))
# print(isvalid_username("abc1 deg"))
# print(isvalid_username("abc deg2"))
# print(isvalid_username("abc2 deg2"))
# print(isvalid_username("abc deg xxe "))
# print("===")
# print(isvalid_username("abc"))
# print(isvalid_username("abc2"))

# for username
while True:
    username = input("Enter your username:")
    try:
        if not isvalid_username(username):
            raise UserNameError("Invalid username!")
        else:
            break
    except UserNameError as ue:
        print(ue)
    except Exception as e:
        print(e)

# for password
# while True:
#     password = input("Enter your password:")



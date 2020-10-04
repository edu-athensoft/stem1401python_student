"""
N.B.: the teacher's version is in Slack 200912f
[Homework]
1. Project: Login Form v4
Adding exception handling to Login Form
Requirements:
User has to input his/her name as username
The username must consist of alphabet and whitespace only
If username contains any other char(s), an error should be raised
User has to input his/her password
The password must contain at least 8 characters
The password must contain at least one capital letter
The password must contain at least one lowercase letter
The password must contain at least one digit (number)
The password must contain at least one symbol
The valid symbols are ! @ # $ % & - _ = [ ] { } < >
If any of the above constraints was not carried out, a proper user-defined exception should be raised.


teacher's way:



step 1. username
    expect the boolean result of checking username if it is valid or not
    case 1. one-word username
    case 2. multiple-word username
    if user input a valid username, program goes on
    else an error should be raised.
step 2. password

class UserNameError(ValueError):
    pass

# case 1.
def isvalid_username(username):
    return username.isalpha()
# test
print(isvalid_username('issa'))
print(isvalid_username('issa2'))
print()

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
"""

# split whitespaces --> look at the string_method_20_split
# and the strip the first and last whitespace of the username


class UserNameError(ValueError):
    pass


class PwdTooShortError(ValueError):
    pass


class PwdCapitalizeError(ValueError):
    pass


class PwdLowercaseError(ValueError):
    pass


class PwdDigitError(ValueError):
    pass


class PwdSymbolError(ValueError):
    pass


"""
# not good
# while True:
#     username = input("Username: ")
#     new_username = username.split()
#     if username.isalpha():
#         break
#     else:
#         raise UserNameError("Invalid username.")
"""

# case 1. --> consists of only one word


# def valid_username(username):
#     return username.isalpha()


# case 2.
# if username has space(s), split the spaces in the original username
def valid_username_2(username):
    new_username = username.split()
    for i in new_username:
        if not i.isalpha():
            return False
    return True


while True:
    username = input("Input your username: ")
    original_username = valid_username_2(username)

    if original_username:
        print(f"{username} is a valid username.")
        break
    else:
        try:
            raise UserNameError("Invalid username. Your username must contain only letters and or whitespaces. Please try again.")
        except UserNameError as ue:
            print(ue)
        except Exception as e:
            print(e)


# now do for password:


characters = ["!", "@", "#", "$", "%", "&", "-", "_", "=", "[", "]", "{", "}", "<", ">"]

while True:
    password = input("Input your password: ")
    length_pwd = len(password)
    if length_pwd >= 8:
        pass
    else:
        try:
            raise PwdTooShortError("Invalid password, your password must contain at least 8 characters. Please try again.")
        except PwdTooShortError as tse:
            print(tse)
        except Exception as e:
            print(e)
    if any(i.isupper() for i in password):
        pass
    else:
        try:
            raise PwdCapitalizeError("Invalid password, your password must contain at least one capital letter. Please try again.")
        except PwdCapitalizeError as ce:
            print(ce)
        except Exception as e:
            print(e)
    if any(i.islower() for i in password):
        pass
    else:
        try:
            raise PwdLowercaseError("Invalid password, your password must contain at least one lowercase letter. Please try again.")
        except PwdLowercaseError as le:
            print(le)
        except Exception as e:
            print(e)
    if any(i.isdigit() for i in password):
        pass
    else:
        try:
            raise PwdDigitError("Invalid password, your password must contain at least one digit. Please try again.")
        except PwdDigitError as de:
            print(de)
        except Exception as e:
            print(e)
    if any(i in characters for i in password):
        print(f"{password} is a valid password.")
    else:
        try:
            raise PwdSymbolError("Invalid password, your password must contain at least one valid symbol. Please try again.")
        except PwdSymbolError as se:
            print(se)
        except Exception as e:
            print(e)
    break

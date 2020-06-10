"""

"""


def is_valid_len(teststr, expected_len):
    strlen = len(teststr)
    if strlen < expected_len:
        return False
    else:
        return True


def has_uppercase(teststr):
    pass


def has_letter():
    pass


def has_digit():
    pass


def has_symbol():
    pass

# prog settings
PWD_MIN_LEN = 6

# user input
user_input = "aksdha"
# user_input = "12345678"
# user_input = "aksdha12345678"

# processing
while True:
    result = is_valid_len(user_input, PWD_MIN_LEN)
    if result: break

    # result = has_uppercase(user_input)
    # if not result: break
    #
    # result = has_letter(user_input)
    # if not result: break
    #
    # result = has_digit(user_input)
    # if not result: break
    #
    # result = has_symbol(user_input)
    # if not result: break

# output result
print("result = {}".format(result))

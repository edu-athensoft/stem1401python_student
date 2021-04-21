"""

"""
import string


def test_fn(filename, extension=".txt"):
    print(f"{filename}{extension}")


def create_file(filename, extension=".txt"):
    with open(f"{filename}{extension}", "x") as file:
        file.close()


for letter in string.ascii_uppercase:
    # print(letter)
    test_fn(letter, '.log')
    # create_file(letter)

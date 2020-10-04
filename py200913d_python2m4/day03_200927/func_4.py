"""
about function

function -> representing a behavior, an action, or an operation

1. docstring
"""


def greeting():
    """
    print out greeting words
    :return:
    """
    print("hello, this is a function!")


docs = greeting.__doc__
print(docs)

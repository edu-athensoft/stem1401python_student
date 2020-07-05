"""
variable function arguments
Python Arbitrary Arguments

def foo(*obj):
    pass

"""


# *names is taken as a tuple
def greet(*names):
    """This function greets all the persons in the names tuple."""
    # TODO

    return names


name_list = greet('Marie', 'Darice', 'Peter')
print(name_list)


# input 'Marie', 'Darice', 'Peter'
# output
#   'How do you do? Marie
#   'How do you do? Darice
#   'How do you do? Peter





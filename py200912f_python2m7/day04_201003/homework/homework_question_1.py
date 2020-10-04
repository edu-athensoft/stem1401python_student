"""
1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
e.g.: User inputs 5
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

# input
user_input = int(input("Input an integer: "))

# generate a dictionary
user_square = {x: x*x for x in range(1, user_input + 1)}

# output
print(user_square)



# version 2.
# decoupled

def gendict(n):
    """
    generate a dictionary by n
    :param n: the number of items in a dictionary
    :return: generated dictionary
    """
    dict1 = {x: x * x for x in range(1, n + 1)}
    return dict1


# main program
# input
user_input = int(input("Input an integer: "))

# generate a dictionary
mydict = gendict(user_input)

# output
print(mydict)


"""
how to validate the number and make it within your upper and lower bound
"""

"""
x = int(input("enter a number (1-100):"))
if x > 100 or x <1:
    print("Warning: Please input a valid number!")
else:
    print("Your input is {}".format(x))
"""

# Leon -  do-while v.s. while

def inputValidNumber():
    x = ''
    while True:
        x = int(input("enter a number (1-100):"))
        if x > 100 or x < 1:
            print("Warning: Please input a valid number!")
        else:
            print("Your input is {}".format(x))
            break
    return x


inputValidNumber()
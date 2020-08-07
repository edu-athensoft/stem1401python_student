"""
infinite loop
"""

# while True:
#     print("The while loop never stops.")


# while 1:
#     print("The while loop never stops.")


# while 'not empty string':
#     print("The while loop never stops.")


while 'not empty string':

    # if user input a command of 'exit'
    # then the infinite loop terminates
    cmd = input("Enter a command:")
    print("{}".format(cmd))
    if cmd == 'exit':
        break



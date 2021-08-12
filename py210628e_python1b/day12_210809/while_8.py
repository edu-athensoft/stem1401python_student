"""
application of while loop

1. os command line, terminal
"""

flag = True

while flag:
    cmd = input("input a command")
    print("execute the command: {}".format(cmd))

    if cmd == 'quit' or cmd == 'q' or cmd == 'exit':
        flag = False
else:
    print('Bye')

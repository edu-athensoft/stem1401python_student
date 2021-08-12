"""
application of while loop

1. os command line, terminal
"""

flag = True

while flag:
    print("execute a command")
    is_cont = input('Do you want to continue?[y|n]')
    # print(is_cont)
    if is_cont == 'n' or is_cont == 'no':
        flag = False



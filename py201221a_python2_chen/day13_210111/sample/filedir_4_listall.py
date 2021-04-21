import os

def printlist(mylist):
    for i in mylist:
        print(i)

def showdir(dirname, level=0):
    dir_list = os.listdir(dirname)
    # printlist(dir_list)  # \u2515
    for name in dir_list:
        print(f'{"  "*level}{name}')
        if os.path.isdir(dirname+os.sep+name):
            level += 1
            showdir(dirname+os.sep+name, level)
            level -= 1

start_path = os.getcwd()+os.sep+'testdir'
start_path = '.'
start_path = '../../'
showdir(start_path)

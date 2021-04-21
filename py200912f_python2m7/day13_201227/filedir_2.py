"""
to test if a path is a dir or file?
"""


import os


path = 'testdir'
path = 'filedir_1.txt'

if os.path.isdir(path):
    print("it's a directory")
elif os.path.isfile(path):
    print("it's a file")
else:
    print("it's a special file like FIFO, device file, socket")

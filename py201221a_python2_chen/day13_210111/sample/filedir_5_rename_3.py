"""
rename files

*.html -> *.txt

from file6.html to file6.txt
from file7.html to file7.txt
from file8.html to file8.txt
...

hints:
loop

how to rename?
file name and directory name are both string.
replace()
file6.html ->

how to get valid file names under a specific directory?
listdir() - return a list of string

"""

import os

def myrename(fname, ext1, ext2):
    """
    rename a file
    :return:
    """
    if fname.endswith('.'+ext1):
        # print(fname)
        # rename
        oldname = fname
        newname = fname.replace('.'+ext1, '.'+ext2)
        os.rename(oldname, newname)


# get file/dir list
path = 'testdir'
EXT1 = 'log'
EXT2 = 'bin'

os.chdir(path)
print(os.getcwd())

names = os.listdir()
print(names)

for fname in names:
    myrename(fname, EXT1, EXT2)









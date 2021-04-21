"""
rename a file

from file6.html to file6.txt

"""

import os

# rename a directory

# before
print(os.listdir('testdir'))

# renaming
oldname = "testdir/dir4"
newname = "testdir/dir5"

os.rename(oldname, newname)

# after
print(os.listdir('./testdir'))







"""
review

1. to get cwd
2. to change the cwd
"""

import os

res = os.getcwd()
print(res)

# changing cwd to testdir
# relative path
os.chdir('testdir')

res = os.getcwd()
print(res)





"""
to rename a directory
to rename a file

rename(src, dest)
"""

import os

# case 1. to rename a dir
# testdir -> testdir1

old = 'testdir'
new = 'testdir1'

os.rename(old, new)

print(os.listdir())


# how to rename 'review_for.py' to 'review_forloop.py'
old = 'review_for.py'
new = 'review_forloop.py'

os.rename(old, new)

print(os.listdir())
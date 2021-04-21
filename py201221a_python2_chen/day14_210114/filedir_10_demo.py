"""
a demo for using os.path.exists()
"""


import os

filename = 'review_1.py'
flag = os.path.exists(filename)

if flag:
    print('Yes, the file does exist.')
else:
    print('Your specified file does not exist.')


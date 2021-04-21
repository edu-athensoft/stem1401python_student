"""
remove a file
"""

import os


currentlist = os.listdir()
print(currentlist)

# remove a file
filepath = 'file_to_remove.txt'
os.remove(filepath)

currentlist = os.listdir()
print(currentlist)

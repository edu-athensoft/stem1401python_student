"""
open a file in read mode
"""

f = open("file5_mode_r.txt",'r')

# read the whole data in the file
print(f.read())

f.close()
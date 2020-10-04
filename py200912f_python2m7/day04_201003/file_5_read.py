"""
open a file in read mode
"""

f = open("file5_mode_r.txt",'r')

# read the specified length of data in the file
print(f.read(8))
print(f.read(8))

print(f.read(8))
print(f.read(8))

f.close()
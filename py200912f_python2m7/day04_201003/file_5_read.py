"""
open a file in read mode
"""

f = open("file5_mode_r.txt",'r')

# read the specified length of data in the file
print(f.read(8),end="==")
print(f.read(8),end="==")
# print(f.read(1),end="==")
# print("EOF",end="==")
# print(f.read(1),end="==")
# print("EOF")

print(f.read(8),end="==")
print(f.read(8),end="==")
print(f.read(8),end="==")

f.close()
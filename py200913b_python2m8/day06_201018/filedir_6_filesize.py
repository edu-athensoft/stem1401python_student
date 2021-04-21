"""
get file size


"""


import os

filename = "filedir_2_mkdir.py"
result = os.path.getsize(filename)

print(result, "bytes")


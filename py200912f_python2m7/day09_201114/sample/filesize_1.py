"""
get file size
Byte
KB
MB
GB
"""

import os

path = "filecopy_1.py"
size = os.path.getsize(path)
print(f"File size of {path} is {size} Bytes")





"""
to get the file size of a specified document

getsize(filename)

os.path.getsize()
"""

import os

filename = "review_1.py"
result = os.path.getsize(filename)

print(result, "bytes")
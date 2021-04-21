"""
rmdir() - remove an empty directory
"""

import os

try:
    dirpath = "testdir"

    if os.path.exists(dirpath):
        os.rmdir(dirpath)


except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

print("done.")
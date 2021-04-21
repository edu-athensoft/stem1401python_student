"""
search path

1. current path
2. pythonpath
3. the installation-dependent directory

"""

import sys

paths = sys.path

for p in paths:
    print(p)
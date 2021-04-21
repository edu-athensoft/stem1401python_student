"""
create a directory

"""

import os


try:
    # step 1. specify a path/dir
    path = 'testdir/dir4'

    # step 2. create the dir
    os.mkdir(path)

except OSError as oe:
    print(oe)

except RuntimeError as rte:
    print(rte)

except Exception as e:
    print(e)





"""


"""


import os

# step 1.
# os.mkdir('dir_to_remove')

# step 2.

try:
    isexists = os.path.exists('dir_to_remove')

    if isexists:
        os.rmdir('dir_to_remove')
    else:
        print("We can not remove a non-existing folder.")

except Exception:
    print('Unknown exception.')


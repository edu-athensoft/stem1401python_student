"""
exception handling with try statement

keywords:
try
except  (exception)

place all the statement that you suspect into a try block
handling captured errors in except block

sys.exc_info()[0]
show or get execution information

syntax:

try:
    pass
except:
    pass


"""

# example


import sys

random_list = ['a',0,2]

r = -1
for entry in random_list:
    try:
        print(f"The entry is {entry}")
        r = 1 / int(entry)
        print(f"The reciprocal of {entry} is {r}")
        break
    except:
        print(f"Oopsm, {sys.exc_info()[0]} occurred")
        print("Next entry")

    print()
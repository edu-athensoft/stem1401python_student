"""
basic syntax of exception handling

keyword: try, except
try-except

"""

import sys

values = ['a',0, 2,'3']

for value in values:
    try:
        result = 1/int(value)
        print(value, result)
    except:
        print("Oops!", sys.exc_info()[0],"occurred.")
        print("Next entry.")
        print()

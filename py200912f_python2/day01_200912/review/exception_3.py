"""

Exception
e.__class__


compare with:
__doc__

"""


# import sys

random_list = ['a',0,2]

r = -1
for entry in random_list:
    try:
        print(f"The entry is {entry}")
        r = 1 / int(entry)
        print(f"The reciprocal of {entry} is {r}")
        break
    except Exception as e:
        print(f"Oopsm, {e.__class__} occurred")
        print("Next entry")

    print()
"""
keyword:  try, except (exception)
"""


def fa():
    print("fa()")
    fb()


def fb():
    print("fb()")
    fc()


def fc():
    print("fc()")
    try:
        # print(a)
        print(1 + "str1")
    except:
        print(sys.exc_info()[0])
        print()



# main program
# call fa()
import sys

print("=== start ===")
fa()
print("=== end ===")
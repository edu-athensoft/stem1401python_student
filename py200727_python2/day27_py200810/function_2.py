"""
why we need function

1. to remove redundant statements
2. to reuse code
"""


# case 1.

# paragraph
def printtext():
    print("sentence1")
    print("sentence2")
    print("sentence3")
    print("sentence4")

# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()

for i in range(127):
    printtext()

print()

# case 2.
def add(num1, num2):
    # num1 = 1
    # num2 = 2

    res = num1 + num2
    print(res)

add(3, 5)









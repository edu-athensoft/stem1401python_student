"""
infinite loop
"""

flag = True

counter = 10

while flag:
    print("infinite loop")
    counter -= 1

    # conditionally
    if counter <= 0:
        flag = False





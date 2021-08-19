"""
keyword: continue

stop the current iteration and move to the next immediately
"""


counter = 0

while counter < 10:
    counter += 1
    # print('execute', counter)  # move it after if-continue


    if counter == 6:
        continue

    print('execute', counter)


print("end")

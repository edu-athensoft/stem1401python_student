"""
keyword: break

constraints:
if counter == 6, exit

the statements after the break statement cannot be reached
"""


# counter = 0
#
# while counter < 10:
#     if counter == 6:
#         break
#
#     print('execute',counter)
#     counter += 1



counter = 0

while counter < 10:
    print('execute',counter)

    if counter == 6:
        break
        # print("after break 1")
        # print("after break 2")

    counter += 1


print("end")

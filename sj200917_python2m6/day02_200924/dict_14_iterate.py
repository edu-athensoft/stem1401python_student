"""
iterating through a dictionary
using a for loop
"""

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

for key in squares:
    # print(key, squares[key])
    print("{}:{}".format(key, squares[key]))
print()

for key in squares.keys():
    print("{}:{}".format(key, squares[key]))


"""
print out 1 x 1, 2 x 1, 2 x 2, ...., 9 x 9
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(i, j, i * j), end="\t")
    print()




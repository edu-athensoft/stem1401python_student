"""
list dirs and files

listdir()
"""

import os

result = os.listdir()

print(type(result))

# print(result)


for item in result:
    print(item)

print("===============")

result2 = os.listdir("../day12_201128")

for item in result2:
    print(item)


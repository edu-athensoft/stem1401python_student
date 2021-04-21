"""
list all subdirectories and files under current working dir
"""



import os

res = os.listdir()
print(type(res))

print(res)


# to print out item one by one
# for loop

for item in res:
    print(item)


# to list all under a specified directory
filepath = 'testdir'

res2 = os.listdir(filepath)
print(res2)








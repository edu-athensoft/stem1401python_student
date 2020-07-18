"""
7/11/2020
Ze Yue Li
[Homework]
Rewrite 6
"""
num = 5
dict1 = {}
for i in range(1, num+1):
    dict1[i] = i*i
print(dict1)


# refactoring
# generic

def getdict(num):
    dict1 = {}
    for i in range(1, num + 1):
        dict1[i] = i * i
    return dict1

# main program
print(getdict(0))
print(getdict(1))
print(getdict(2))
print(getdict(3))
print(getdict(5))
print(getdict(-1))
# print(getdict('abc'))

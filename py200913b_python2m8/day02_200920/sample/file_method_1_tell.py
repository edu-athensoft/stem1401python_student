"""
file method:
tell()
tell v.s. seek
"""


f = open("test.txt")
location = f.tell()
print(f'location = {location}')

result = f.__next__()
print(result,end="")

result = f.__next__()
print(result,end="")

result = f.fileno()
print(result)
f.close()
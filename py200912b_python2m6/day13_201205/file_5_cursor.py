"""
file cursor

tell()
"""


file = open("homework/myweb.html")

content = file.read(15)

print(content)

pos = file.tell()

content = file.read(1)
print(content)
pos = file.tell()
print(f"pos = {pos}")

content = file.read(1)
print(content)
pos = file.tell()
print(f"pos = {pos}")

content = file.read(1)
print(content)
pos = file.tell()
print(f"pos = {pos}")

content = file.read(1)
print(content)
pos = file.tell()
print(f"pos = {pos}")

content = file.read(1)
print(content)
pos = file.tell()
print(f"pos = {pos}")

content = file.read(1)
print(content)
pos = file.tell()
print(f"pos = {pos}")

content = file.read(1)
print(content)
pos = file.tell()
print(f"pos = {pos}")

print("=================",end="\n")




print("=================")
file.close()
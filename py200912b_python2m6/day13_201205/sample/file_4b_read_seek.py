"""
read utf-8

tell()
"""

f = open("file_6.txt", encoding="utf-8")
print(f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

f.seek(0)
print("after seek(0) = ",f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

content = f.read(1)
print(content, f.tell())

# f.seek(17)  # failed
f.seek(32)  # failed

content = f.read(1)
print(content, f.tell())

f.close()
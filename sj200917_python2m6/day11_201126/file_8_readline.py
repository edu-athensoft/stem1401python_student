"""
read a file line by line
readline()
"""

file = open("file7.txt", encoding="utf-8")

print("======")

# line 1
content = file.readline()
print(content, end="")

# line 2
content = file.readline()
print(content, end="")

# line 3
content = file.readline()
print(content, end="")

# line 4
content = file.readline()
print(content, end="")

# line 5
content = file.readline()
print(content, end="")

# line 6
content = file.readline()
print(content, end="\n")
print("======")

file.close()

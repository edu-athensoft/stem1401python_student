"""
file
readline()

checksum

"""
file = open("file_1.txt", encoding="utf-8")

# size - integer
print("===")
content = file.readline()
print(content, end="")

content = file.readline()
print(content, end="")

content = file.readline(500)
print(content, end="")

content = file.readline(-1)
print(content, end="")


print("===")

file.close()


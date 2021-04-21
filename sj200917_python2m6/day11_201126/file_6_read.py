"""
read a file
read()
"""

# 1. open
file = open("file6.txt")

# 2. read
content = file.read()
print("====")
print(content)
print("====")

# 3. close
file.close()

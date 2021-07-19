"""
demo of reading a file
"""


with open('COLORS','r') as file:
    result = file.readlines()

print(result)


for item in result:
    item = item.strip()
print(result)


for i in range(len(result)):
    result[i] = result[i].strip()

print(result)
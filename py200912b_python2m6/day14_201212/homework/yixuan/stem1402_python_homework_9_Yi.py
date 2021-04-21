# Read html and copy

file = open("home1.html")

content = file.read()

file = open("stem1402_python_homework_9.2_Yi.py", 'w')

file.write(content)

file.close()

print()
print()

# Read csv and copy

file = open("csv.url")

content = file.read()

file = open("stem1402_python_homework_9.2_Yi.py", 'a')

file.write(content)

file.close()

print()
print()
# read half and copy

file = open("csv.url")
file.read

lines = int(len(file.readlines())/2)
file.seek(0)

file1 = open("stem1402_python_homework_9.2_Yi.py", 'a')

for i in range(lines):
    content = file.readline()
    file1.write(content)
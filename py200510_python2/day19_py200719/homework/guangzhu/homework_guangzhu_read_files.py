"""
19/07/2020
Guang Zhu Cui
[Homework]
1. Read a text-based file
2. Read a python source code file
"""
# 1. Read a text base file
print('[info] open file in current directory')
print('[info] openning homework_text_file_to_read ...')
file = open("homework_text_file_to_read.txt")
content = file.read(6)
print(content)
file.close()
print('[info] done')
print('\n','\n')

# 2. Read a python source code file
print('[info] open file in current directory')
print('[info] openning homework_python_file_to_read ...')
file = open("homework_python_file_to_read.py")
content = file.read()
print(content)
file.close()
print('[info] done')

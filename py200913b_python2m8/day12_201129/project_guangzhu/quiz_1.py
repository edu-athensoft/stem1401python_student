"""
write a program to rename multiple files in a specific directory
"""
#assuming 1
import os
numbers = [1,2,3]
for i in numbers:
    os.renames(f'file_{i}.html',f'file_{i}.txt')
#name back
name_back = input('do you want to name back the files(y/n)?:')
if name_back == 'y':
    for i in numbers:
        os.renames(f'file_{i}.txt',f'file_{i}.html')
else:
    print('files renamed')


"""
2. Calculate the size of a directory
"""
import os


def get_size():
    start_path = input('Please enter the full path of the directory:')
    size = 0
    for dir_path, dir_names, file in os.walk(start_path):
        for f in file:
            file_path = os.path.join(dir_path, f)
            stat = os.stat(file_path)
            size += stat.st_size

    return size


print(get_size(), 'bytes')




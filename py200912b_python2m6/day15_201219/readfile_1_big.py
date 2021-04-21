"""
read large file in chunks

read()
read(size)
readline()
readline(size)
readlines()

chunk
"""

def read_in_chunks(file_path,  chunk_size=1024*1024):
    """
    Lazy function (generator) to read a file piece by piece
    1 MB per chunk by default
    :param file_path:
    :param chunk_size:
    :return:
    """
    file_object = open(file_path)

    while True:
        chunk_data = file_object.read(chunk_size)

        if not chunk_data:
            break

        yield chunk_data


# main
filepath = 'file_large_1.txt'

# read_in_chunks(filepath, 10)
content = read_in_chunks(filepath)
print(list(content))

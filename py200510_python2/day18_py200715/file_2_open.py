"""
File explorer
Finder

file, directory

File is a named location on disk to store related information.


open()
"""

# case 2. open file in current directory which does not exist
print("[info] open file in current directory")
print("[info] opening file1_open_b.txt ...")

try:
    f = open("file1_open_b.txt")

    print("[info] closing ...")
    f.close()

    print("[info] done.")
except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)



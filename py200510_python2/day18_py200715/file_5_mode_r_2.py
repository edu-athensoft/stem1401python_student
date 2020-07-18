"""
file mode:  r (t)
"""

print("[info] open file in current directory")
print("[info] opening file5_mode_r.txt ...")

try:
    f = open("file5_mode_r.txt", 'r')

    # read specified bytes of data from specified position
    # seek(pos)
    # read(bytes)
    f.seek(4)
    content = f.read(10)

    # display the content
    print(content)

    f.seek(0)
    content = f.read(10)
    print(content, end="")

    content = f.read(10)
    print(content)

    f.close()
    print("[info] done.")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

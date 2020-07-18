"""
file mode:  r (t)
"""

print("[info] open file in current directory")
print("[info] opening file5_mode_r.txt ...")

try:
    f = open("file5_mode_r.txt", 'r')

    # read all data from the file
    content = f.read()

    # display the content
    print(content)

    f.close()
    print("[info] done.")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

"""
file mode:  r (t)
readline

"""

print("[info] open file in current directory")
print("[info] opening file5_mode_r.txt ...")

try:
    f = open("file5_mode_r.txt", 'r', encoding="utf-8")

    # read
    content = f.readline()

    # read by size
    line = f.readline(4)
    print(line)

    # read next line
    # content = f.readline()

    #
    # f.seek(0)
    # content = f.readline()
    #
    #
    # content = f.readline()
    # content = f.readline()
    # content = f.readline()
    # content = f.readline()
    #
    # # last line (blank)
    # content = f.readline()
    #
    # # read extra line
    # content = f.readline()
    # content = f.readline()
    #
    # # display the content
    # print(content)

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
    print("[info] done.")

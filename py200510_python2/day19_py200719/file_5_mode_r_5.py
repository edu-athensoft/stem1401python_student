"""
file mode:  r (t)
readlines()

"""

print("[info] open file in current directory")
print("[info] opening file5_mode_r.txt ...")

try:
    f = open("file5_mode_r.txt", 'r', encoding="utf-8")

    # read
    content = f.readlines()

    print(content)

    # output the content
    for line in content:
        print(line, end="")


except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
    print("[info] done.")

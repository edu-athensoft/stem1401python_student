"""
file mode:  r (t)
immediately open and read

"""

print("[info] open file in current directory")
print("[info] opening file5_mode_r.txt ...")

try:
    # f = open("file5_mode_r.txt", 'r', encoding="utf-8")

    for line in open("file5_mode_r.txt", 'r'):
        print(line, end="")


except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    # f.close()
    print("[info] done.")

"""
file mode:  r (t)
immediately open and read

"""

print("[info] open file in current directory")
print("[info] opening file5_mode_r.txt ...")

try:
    with open("file5_mode_r.txt1", 'r') as file:
        content = file.readlines()
        for line in content:
            print(line, end="")
except FileNotFoundError as fe:
    print(fe)

print("[info] done.")
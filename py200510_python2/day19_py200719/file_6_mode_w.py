"""
file mode w - write

"""

# case1. truncates
try:
    f = open("file6_mode_w.txt",'w')

    content = "this is the new content to write"
    charnum = f.write(content)

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()


# case2. create
f = open("file6_mode_w_create.txt",'w')

content = "this is the file to create"
charnum = f.write(content)
f.close()

print(f"charnum={charnum}")


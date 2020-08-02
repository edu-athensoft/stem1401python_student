
str1 = "The quick brown fox jumps over the lazy dog"
dumb = str1.split()
yet = int(input("Please input a number:"))
str2 = []
for i in dumb:
    if len(i) > yet:
        str2.append(i)

print(str2)



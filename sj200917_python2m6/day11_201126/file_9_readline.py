"""
read a file line by line
readline()
"""

print(not "abc")



file = open("file8.txt", encoding="utf-8")

print("======")

while True:
    content = file.readline()
    print(content, end="")

    # if the line is not absolutely empty, then continue, or else break to stop
    if not content:
        break

    # if content:
    #     continue
    # else:
    #     break

print("\n======")

file.close()

"""
writelines()

readlines()
"""

try:
    file = open("filemode_2.txt",'a')

    content_list = ["See you later!", "Good bye!", "See you tomorrow!"]

    file.writelines(content_list)

    content_list = ["\n","See you later!\n", "Good bye!\n", "See you tomorrow!\n"]

    file.writelines(content_list)
    file.close()



    file = open("filemode_3.txt")

    content = file.readlines()

    print(content)
    print("====")
    for line in content:
        print(line)

    file.close()

except Exception as e:
    print(e)
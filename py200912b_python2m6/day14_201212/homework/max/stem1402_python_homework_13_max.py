"""

"""

# 1.
try:
    file1 = open("stem1402_python_homework_13_max.html", 'r')

    content = file1.read()

    file2 = open("stem1402_python_homework_13_max_copy.html", 'w')

    file2.write(content)
    file1.close()
    file2.close()

except Exception as e:
    print(e)

except FileNotFoundError as fe:
    print(fe)


# 2.
try:
    file1 = open("stem1402_python_homework_13_max.csv", 'r')

    content = file1.read()

    file2 = open("stem1402_python_homework_13_max_copy.csv", 'w')

    file2.write(content)
    file1.close()
    file2.close()

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)


# 3.
try:
    file1 = open("stem1402_python_homework_13_max.csv", 'r')

    lines = int(len(file1.readlines())/2)
    file1.seek(0)

    # file2 = open("stem1402_python_homework_13_max_copy_2.csv", 'a')
    file2 = open("stem1402_python_homework_13_max_copy_2.csv", 'w')

    for i in range(lines):
        content = file1.readline()
        file2.write(content)

    # close file
    file1.close()
    file2.close()

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)












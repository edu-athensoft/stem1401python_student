"""
plus

r+
[Homework] 201107
a+    -->    [homework]
w+    -->    [homework]

text file - t
binary file - b
"""

"""
Goal: trying out read and write (r+)
"""
# r+ --> this is correct :)
try:
    file = open('homework_html.html', 'r+')
    print(file.read())
    file.write("\nNew content")
    file.close()

    file = open('homework_html.html', 'r')
    print(file.read())
    file.close()

except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
# finally:
#     file.close()

"""
Goal: trying out read and write (w+)
"""
try:
    file = open('homework_html.html', 'w+')
    file.write("\nIssa is the best!!!")
    file.seek(0)
    print(file.read())
    file.close()

except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
# finally:
#     file.close()

"""
Goal: trying out read and write (a+)
"""

try:
    file = open('homework_html.html', 'a+')
    file.write("\nIssa is a basketball player!!!")
    print(file.read())
    file.close()

except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
# finally:
#     file.close()

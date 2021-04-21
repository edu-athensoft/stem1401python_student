"""
stem1402_python_homework_11_steven
"""

print("HTML")
try:
    print("Start opening file...")
    file = open("stem1402_python_homework_9.html", encoding="utf-8")
    print("=============================")
    content = file.read()
    file = open("stem1402_python_homework_11_steven_html", 'w')
    file.write(content)
    file.close()
    print("Content has been written.")

except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)
print("Done.")
print()


print("CSV")
try:
    print("Start opening file...")
    file = open("stem1402_python_homework_9.csv", encoding="utf-8")
    print("=============================")
    content = file.read()
    file = open("stem1402_python_homework_11_steven_cvs", 'w')
    file.write(content)
    file.close()
    print("Content has been written.")

except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)
print("Done.")
print()


# I didn't find the answer for this question
print("HALF CSV")
try:
    print("Start opening file...")
    file = open("stem1402_python_homework_9.csv", encoding="utf-8")
    print("=============================")

    content = file.read()
    file = open("stem1402_python_homework_11_steven_cvs_half", 'w')
    file.write(str(content))
    file.close()
    print("Content has been written.")

except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)
print("Done.")
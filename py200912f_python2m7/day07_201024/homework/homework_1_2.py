"""
[Homework]
1. Write a program to read a text file and calculate how many lines it contains.
2. Write a program to read a text file and calculate what size (how many characters) it is (it has).
"""

# q1
try:
    # file = open("homework_html.html", 'r')
    file = open("homework_html.html")
    result = file.readlines()
    # print(len(result))
    print(f"The document contains {len(result)} lines.")

except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    file.close()


# q2
try:
    file = open("homework_html.html", 'r')
    result_2 = file.read()
    # print(len(result_2))
    print(f"The document contains {len(result_2)} characters.")

except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    file.close()

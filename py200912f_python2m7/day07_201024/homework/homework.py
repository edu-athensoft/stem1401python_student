"""
[Homework]

1. Read an HTML document and print it out
"""
try:
    open_file = open("homework_html.html", 'wt')
    read_file = open_file.read()  # open_file.readable --> result = False
    print(read_file)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    open_file.close()

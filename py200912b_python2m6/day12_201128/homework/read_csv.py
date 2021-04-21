"""
[Homework]
1. Search and Download an html file
Read it and print out

html - Hypertext Markup Language
render


2. Search and Download a CSV file
Read it and print out

data source, data file
big data

csv - data
log - log file
"""

print("Starting load html document...")
try:
    file = open("csvdata.csv")

    content = file.read()

    print(content)

    file.close()
except FileNotFoundError as fe:
    print(fe)
except IOError as ie:
    print(ie)
except Exception as e:
    print(e)
else:
    print("Done.")

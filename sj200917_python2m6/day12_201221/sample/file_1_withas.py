"""
with ... as
"""

# case 1.
with open("homework_html.html") as file:
    content = file.read()
    print(content, end="")

print()


# case 2. File does not exist
try:
    with open("homework_html.html11") as file:
        content = file.read()
        print(content, end="")
except FileNotFoundError as e:
    print(e)

"""
with ... as
"""



# in traditional way

file = open('text14.txt')
content = file.read()
file.close()

# rewrite
file = open('text14.txt')
try:
    content = file.read()
finally:
    file.close()


# rewrite
with open('text14.txt') as file:
    content = file.read()
"""
with as
"""

file = open("/tmp/foo.txt")
try:
    data = file.read()
except Exception as e:
    pass
finally:
    file.close()


# 2
with open("/tmp/foo.txt") as file:
    data = file.read()



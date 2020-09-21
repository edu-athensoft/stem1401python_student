"""
dictionary
update()

"""

d = {'x': 2}

# tuple auto-packing
d.update(y = 3, z = 0)
print(d)


# (('y',3),('z',0))

# nested list
d.update([['a', 3], ['b', 0]])
print(d)

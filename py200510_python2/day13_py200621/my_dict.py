"""

"""

# fromkeys(seq[, v])

marks = {}.fromkeys(['Math','English','Science'])
print(marks)
print()

marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)
print()

marks = {}.fromkeys(['Math','English','Science'], "")
print(marks)
print()


# items()
for item in marks.items():
    print(item)

# keys()
mykeys = marks.keys()
print(mykeys,type(mykeys))
print(list(mykeys))
print(list(sorted(mykeys)))
print(list(sorted(mykeys,reverse=True)))

# values()
marks['Math'] = 'mv'
marks['English'] = 'ev'
marks['Science'] = 'sv'
myvalues = marks.values()
print(myvalues,type(myvalues))
print(list(myvalues))

# update([])
marks.update([['Science','sv2']])
print(marks)

d = {'x': 2}

d.update(y = 3, z = 0)
print(d)

d.update([['a', 3], ['b', 0]])
print(d)

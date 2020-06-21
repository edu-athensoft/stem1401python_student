"""
remove element

pop(key)
popitem()
clear()
del
"""

stu1 = {"name": "Jackie", "age": 26,"score":98, "grade":'A'}
print(stu1, type(stu1))

# pop(key)
stu1.pop("grade")
print(stu1)

stu1 = {"name": "Jackie", "age": 26,"score":98, "grade":'A'}
v1 = stu1.pop("grade")
print(v1)


# popitem() - arbitrary item (k:v)
stu1 = {"name": "Jackie", "age": 26,"score":98, "grade":'A'}
print(stu1.popitem())


# clear()
stu1 = {"name": "Jackie", "age": 26,"score":98, "grade":'A'}
stu1.clear()
print(stu1)

# del - keyword
stu1 = {"name": "Jackie", "age": 26,"score":98, "grade":'A'}

# remove k:v pair
del stu1["score"]
print(stu1)

# remove dict object
del stu1
print(stu1)





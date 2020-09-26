"""


"""


# q2.
dict2={1:10, 2:20}
dict3={3:30, 4:40}
dict4={5:50,6:60}

dict2.update(dict3)
dict2.update(dict4)
print(dict2)


# q2.b
result = dict2.copy()
result.update(dict3)
result.update(dict4)
print(result, type(result))

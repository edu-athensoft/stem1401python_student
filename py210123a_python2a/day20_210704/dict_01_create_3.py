"""
student profiles as a dictionary

dict_namelist3 = {
    'class1' : {'Peter','Sahar','Tom','Amy'},
    'class2' : {'Jack','Mike','Jessica'}
}
"""

dict_stuprofiles = {
    'class1': {
        's101': {
            'stuid': 's101',
            'name': 'Peter',
            'dob': '1995-01-02',
            'grade': 'G7'
        },
        's102': {
            'stuid': 's102',
            'name': 'Sahar',
            'dob': '1995-03-06',
            'grade': 'G7'
        }
    },
    'class2': {
        's201': {
            'stuid': 's201',
            'name': 'Jack',
            'dob': '1994-01-02',
            'grade': 'G8'
        },
        's202': {
            'stuid': 's202',
            'name': 'Mike',
            'dob': '1994-03-06',
            'grade': 'G8'
        }
    },
    'class3': {
        's301': {
            'stuid': 's301',
            'name': 'Bill',
            'dob': '1996-01-02',
            'grade': 'G6'
        }
    }
}

print(dict_stuprofiles)


# how to get a key-value pair
# to get student profiles of class1

# get() - get value by specified key
result = dict_stuprofiles['class1']
print(type(result))
print(result)

# how to get all the student profiles of class2
key2 = 'class2'
result = dict_stuprofiles[key2]
print(result)

# what if we get value by a non-existing key?
# key4 = 'class4'
# result = dict_stuprofiles[key4]
# print(result)
# KeyError: 'class4'

# get value by a non-existing key without error
key4 = 'class4'
result = dict_stuprofiles.get(key4)
print(result)









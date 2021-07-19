"""
dict
create
"""


# key as string
dict1 = {
    'mon': 'Monday',
    'tue': 'Tuesday',
    'wed': 'Wednesday'
}

print(dict1)

# key as tuple
dict2 = {
    (1,1) : 'tuple 1',
    (2,2) : 'tuple 2',
    (3,3) : 'tuple 3'
}

print(dict2)

# key as boolean
dict3 = {
    True : 'T',
    False: 'F'
}
print(dict3)



# complex values
print()

# case 1. value as a list
dict_namelist = {
    'class1' : ['Peter','Sahar','Tom','Amy'],
    'class2' : ['Jack','Mike','Jessica']
}
print(dict_namelist)

# case 2. value as a tuple
dict_namelist2 = {
    'class1' : ('Peter','Sahar','Tom','Amy'),
    'class2' : ('Jack','Mike','Jessica')
}
print(dict_namelist2)

# case 3. value as a dict
dict_namelist3 = {
    'class1' : {'Peter','Sahar','Tom','Amy'},
    'class2' : {'Jack','Mike','Jessica'}
}
print(dict_namelist3)


"""
goals:  to represent profiles of all students in all classes at our school.

student profile:
student id
first name
last name
dob (date of birth :  yyyy-mm-dd)
previous school
registration date
permanent code

how to choose a key for a student profile?
candidate keys:
1a. first name + last name
1b. first name + last name + (student id)
1c. first name + last name + dob
2. student id
3. permanent code (issued by Quebec edu dept.)

"""


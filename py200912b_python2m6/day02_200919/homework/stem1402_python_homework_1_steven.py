"""
stem1402_python_homework_1_steven
"""

# 1. Define a python dictionary to represent a real thing in the world.
dict1 = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}

# 2. Access every item in the dictionary defined by you in Question 1 by iteration. Print out necessary information in proper layout.
for i in dict1 :
    print(f"The {i} month of the year is {dict1[i]}.")
print()
print()
print("--------------------------------------------------------------")



# 3. Define a nested dictionary to represent a real thing in the world. Choose proper keys.
student_profiles = {
    '01': {'stuid':'01',
           'stufname':'Johnny',
           'stulname':'Blue',
           'gender':'Male',
           'dob':'2008-09-01',
           'schg':'first grade'},

    '02': {'stuid':'02',
           'stufname':'Emma',
           'stulname':'Green',
           'gender':'Female',
           'dob':'2006-12-01',
           'schg':'third grade'},

    '03': {'stuid':'03',
           'stufname':'Jimmy',
           'stulname':'White',
           'gender':'Male',
           'dob':'2007-10-01',
           'schg':'second grade'}

}

# 4. Access the item (entry) in the dictionary defined by you in Question 3 by specified key. The key should be input by users. Print out necessary information in proper layout.

print("(01)")
print("(02)")
print("(03)")
print()
choice1 = input("Which student profile do you wish to see:")
print()
print("--------------------------------------------------------------")

profile1 = student_profiles["01"]
profile2 = student_profiles["02"]
profile3 = student_profiles["03"]

if choice1 == "01":
    print("(stuid) = student ID")
    print("(stufname) = student first name")
    print("(stulname) = student last name")
    print("(gender)")
    print("(dob) = date of birth")
    print("(schg) = school grade")
    print()
    choice2 = input("Please write the abbreviated information about this person do you wish to see:")
    print()

    if choice2 == "stuid":
        print(f"profile1['stuid']:{profile1['stuid']}")
    if choice2 == "stufname":
        print(f"profile1['stufname']:{profile1['stufname']}")
    if choice2 == "stulname":
        print(f"profile1['stulname']:{profile1['stulname']}")
    if choice2 == "gender":
        print(f"profile1['gender']:{profile1['gender']}")
    if choice2 == "dob":
        print(f"profile1['dob']:{profile1['dob']}")
    if choice2 == "schg":
        print(f"profile1['schg']:{profile1['schg']}")

if choice1 == "02":
    print("(stuid) = student ID")
    print("(stufname) = student first name")
    print("(stulname) = student last name")
    print("(gender)")
    print("(dob) = date of birth")
    print("(schg) = school grade")
    print()
    choice2 = input("Please write the abbreviated information about this person do you wish to see:")
    print()

    if choice2 == "stuid":
        print(f"profile2['stuid']:{profile2['stuid']}")
    if choice2 == "stufname":
        print(f"profile2['stufname']:{profile2['stufname']}")
    if choice2 == "stulname":
        print(f"profile2['stulname']:{profile2['stulname']}")
    if choice2 == "gender":
        print(f"profile2['gender']:{profile2['gender']}")
    if choice2 == "dob":
        print(f"profile2['dob']:{profile2['dob']}")
    if choice2 == "schg":
        print(f"profile2['schg']:{profile2['schg']}")

if choice1 == "03":
    print("(stuid) = student ID")
    print("(stufname) = student first name")
    print("(stulname) = student last name")
    print("(gender)")
    print("(dob) = date of birth")
    print("(schg) = school grade")
    print()
    choice2 = input("Please write the abbreviated information about this person do you wish to see:")
    print()

    if choice2 == "stuid":
        print(f"profile3['stuid']:{profile3['stuid']}")
    if choice2 == "stufname":
        print(f"profile3['stufname']:{profile3['stufname']}")
    if choice2 == "stulname":
        print(f"profile3['stulname']:{profile3['stulname']}")
    if choice2 == "gender":
        print(f"profile3['gender']:{profile3['gender']}")
    if choice2 == "dob":
        print(f"profile3['dob']:{profile3['dob']}")
    if choice2 == "schg":
        print(f"profile3['schg']:{profile3['schg']}")

# using function to shorten your code
# reuse - function
# argument - stuid: string

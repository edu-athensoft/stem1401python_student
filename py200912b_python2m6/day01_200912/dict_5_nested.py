"""
a dictionary of a dictionary

nested dictionary
"""

# a profile dataset of a company

"""
There is a company who has a couple of employees
employee 1:
    empid:      001
    empfname:   Peter
    emplname:   White
    gender:     Male
    dob:        1990-09-01
    division:   Marketing
    salary:     5000
    
employee 2:
    empid:      002
    empfname:   (You decide)
    emplname:   (You decide)
    gender:     (You decide: Male|Female|Other)
    dob:        (You decide: yyyy-mm-dd)
    division:   (You decide)
    salary:     (You decide: integer)
    
employee 3:
    empid:      003
    empfname:   (You decide)
    emplname:   (You decide)
    gender:     (You decide: Male|Female|Other)
    dob:        (You decide: yyyy-mm-dd)
    division:   (You decide)
    salary:     (You decide: integer)
"""

# select proper keys

company_profiles ={
    '001': {'empid':'001',
            'empfname':'Peter',
            'emplname':'White',
            'gender':'Male',
            'dob':'1990-09-01',
            'division':'Marketing',
            'salary':5000},
    '002': {'empid':'002',
            'empfname':'Andy',
            'emplname':'White',
            'gender':'Female',
            'dob':'1991-09-12',
            'division':'Admin',
            'salary':4000},
    '003': {'empid':'003',
            'empfname':'Jack',
            'emplname':'White',
            'gender':'Male',
            'dob':'1985-10-12',
            'division':'R&D',
            'salary':8000}
}

# query for employee 001
profile1 = company_profiles['001']
print(profile1)
print(f"profile1['division'] : {profile1['division']}")
print(f"profile1['salary'] : {profile1['salary']}")
print()

profile1 = company_profiles['002']
print(profile1)
print(f"profile1['division'] : {profile1['division']}")
print(f"profile1['salary'] : {profile1['salary']}")
print()

profile1 = company_profiles['003']
print(profile1)
print(f"profile1['division'] : {profile1['division']}")
print(f"profile1['salary'] : {profile1['salary']}")


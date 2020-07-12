"""
The setdefault() returns:

value of the key if it is in the dictionary

None if key is not in the dictionary and default_value is not specified

default_value if key is not in the dictionary and default_value is
specified
"""

# Example 1: How setdefault() works when key is in the dictionary?
person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)
print()


# Example 2: How setdefault() works when key is not in the dictionary?
person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age)


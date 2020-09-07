'''
dictionary

Python dictionary is an unordered collection of items.

key-value pair
dictionary v.s. set

creating dictionary
'''

# creating a dictionary
prod = {
    1 : 'apple',
    2 : 'ball',
    3 : 'battery'
}
print(prod)

# creating an empty dictionary
items = {}
print(items, type(items))


# creating a dictionary
friends = {
    'Jack' :  'Jack Hill',
    'Joe'  :  'Joe Miller',
    'Peter' :  'Peter Wong',
    'Amy' : 'Amy White'
}
print(friends)

# creating a dictionary 2
# profile = studentId, fullName, grade, groupNumber
profiles ={
    's19001' : ['s19001', 'Jack Hill', 'G7', 'GROUP1701'],
    's19002' : ['s19002', 'Joe Miller', 'G8', 'GROUP1801'],
    's19003' : ['s19003', 'Peter Wong', 'G6', 'GROUP1601'],
    's19004' : ['s19004', 'Amy White', 'G7', 'GROUP1702']
}
print(profiles)


# ex. create a dictionary for days of week
# MON -> MONDAY
days_of_the_week = {
    'MON': 'Monday',
    'TUE': 'Tuesday',
    'WED': 'Wednesday',
    'THU': 'Thursday',
    'FRI': 'Friday',
    'SAT': 'Saturday',
    'SUN': 'Sunday'
}
print(days_of_the_week)



# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)

#
my_dict = dict([(1,'apple'),(2,'ball')])
print(my_dict)

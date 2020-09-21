"""
access data from a dictionary

get()
[]

"""
my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name'])

print(my_dict.get('age'))

# KeyError: 'address'
# print(my_dict['address'])

print(my_dict.get('address'))
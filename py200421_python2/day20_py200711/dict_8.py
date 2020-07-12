"""
dictionary
change or add element in a dictionary?

A dictionary in python is mutable

"""

my_dict = {
    "name":'Jack',
    "age": 16
}
print(my_dict)

# case 1. update
# update 'Jack' to 'Peter'
my_dict['name'] = 'Peter'

# output
print(my_dict)


# case 2. add
my_dict['score'] = 99
print(my_dict)

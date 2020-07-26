"""
collection
    list    literal
    tuple   literal
    set     literal
    dict (dictionary)   literal
"""

# list
# ordered sequence, contains 0..n items (elements)
fruitlist = ['apple','mango','orange','banana','pineapple']
fruits = ['apple','orange','banana','pineapple','mango']

print(fruitlist)
print(fruits)


# tuple
# ordered sequence, contains 0..n items(elements)
tuple1 = (1,2,3,4,5,6,7)
print(tuple1)

tuple2 = ('apple','orange','banana','pineapple','mango')
print(tuple2)


# set
# unique item, unordered collection
set1 = {'apple','orange','banana','pineapple','mango'}
print(set1)

set2 = {'apple','orange','apple','banana','pineapple','banana','mango'}
print(set2)

# dictionary, dict
# URL = https://www.microsoft.com/en-ca/
dict1 = {
    'scheme': 'https',
    'host': 'www.microsoft.com',
    'port': 80,
    'app': 'en-ca'
}

dict2 = {
    1: 'mon',
    2: 'tue',
    3: 'wed'
}

print(dict2)





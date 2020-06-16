"""
literal collection

collection - list
collection - tuple
collection - set
collection - dictionary
"""

# list
list_fruit = ['apple', 'peach', 'orange','pineapple']
list_stationary = ['pen','pencil','ruler','notebook','eraser']
print(list_fruit)
print(list_stationary)

fruits = ['apple', 'peach', 'orange','pineapple']

print(list_fruit[0])
list_fruit[0] = 'watermelon'
print(list_fruit)

# tuple
tuple_fruit = ('apple', 'peach', 'orange','pineapple')
tuple_fruit2 = ('orange','pineapple','apple', 'peach')
tuple_fruit3 = ('watermelon', 'peach', 'orange','pineapple','banana')

# tuple_fruit[0] = 'orange'
print(tuple_fruit[0])
print(tuple_fruit[1])
print(tuple_fruit[2])
print(tuple_fruit[3])


# set
# set is unordered
# items in a set must be unique
my_food = {'egg','milk','bread','ham','tomato'}
print(my_food)

my_number = {1,2,3,1,2,3}
print(my_number)

list_students= ["Cuba","Colombia","US","Cuba","Cuba","Colombia","France","France"]

# how many places did people go during spring break?
set_places = {"Cuba","Colombia","US","Cuba","Cuba","Colombia","France","France"}
print(set_places)


# dictionary
# dict
dict_day_of_week = {
    "MON" : "Monday",
    "TUE" : "Tuesday",
    "WED" : "Wednesday",
    "THU" : "Thursday",
    "FRI" : "Friday",
    "SAT" : "Saturday",
    "SUN" : "Sunday"
}

print(dict_day_of_week)

print(dict_day_of_week["MON"])











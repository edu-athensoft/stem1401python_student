"""
map()
original list of number is [1,2,3,4,5,6,7,8,9,10]
double every item of the above list
return and output the new list
"""

original_list = [1,2,3,4,5,6,7,8,9,10]
print(original_list)

a = map(lambda x: 2*x, original_list)
print(a, type(a))

print(list(a))



"""
lambda [1,2,3,4,5,6,7,8,9,10]
square number of each item
and print out the result
in one statement
"""

print(list(map(lambda x: x**2, original_list)))


# homework
"""
[1,2,3,4,5,6,7,8,9,10]
[1,9,25,49,81]
"""
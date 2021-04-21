"""
filter

pick up all even numbers from a list
"""


my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# solution 1. for
new_list = []

for i in my_list:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)



# solution 2. lambda
# filter(function, iterable)


print( list( filter(lambda i: i%2==0 ,  my_list) ) )



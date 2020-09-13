# accessing tuple element(s)
my_tuple = ('p','e','r','m','i','t')
c1 = my_tuple[0]
print(c1)

# a string is actually a tuple of char
my_tuple2 = "hello"
print(my_tuple2)
c2 = my_tuple2[0]
print(c2)

# get the last char of my_tuple and print it out
print(my_tuple[5])

# using negative index
print(my_tuple[-1])
print(my_tuple[-2])
print()

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# get the 'o'
print(n_tuple[0][1])
# get the number of 4
print(n_tuple[1][1])
# get the number of 3
print(n_tuple[2][2])




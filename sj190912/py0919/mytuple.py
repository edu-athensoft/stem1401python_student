# datatype - tuple

# (1,2,3)
# ('1','2','3')
# ('a','b','c')

# a string is a sequence of character

# to create a tuple
my_tuple = (1, 2, 3)
print(my_tuple)

# different type of data
my_tuple2 = (1, 'abc', 'cba', 22)
print(my_tuple2)

# nested tuple
my_tuple2 = (1, my_tuple, 'cba', 22)
print(my_tuple2)

# nested tuple 2
my_list = ['a', 'b', 6, 7.3]
my_tuple2 = (1, my_tuple, my_list ,22)
print(my_tuple2)

# create a tuple without ()
my_tuple3 = 5, 6, 7
print(my_tuple3)

# unpacking tuple
a,b,c = my_tuple3
print(a)
print(b)
print(c)

# tuple with only element
# (2+3)x4 = 20
# 2+3x4 = 14
# (6) = 6
my_tuple4 = (6,)
my_list = [6]
print(my_tuple4)




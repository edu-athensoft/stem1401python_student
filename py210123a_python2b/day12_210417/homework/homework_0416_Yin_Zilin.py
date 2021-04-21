"""
1. Write a Python program to create a tuple with different data types.
2. Write a Python program to unpack a tuple in several variables.
3. Write a Python program to check if there exists repeated items in a given tuple.
"""

# 1

tuple1 = ("Bob",False, 3.2)
print(tuple1, type(tuple1))

# 2

x, y, z = 'a','b','c'
print(x)
print(y)
print(z)



# 3

tuple2 = ('a','a','b','c','d')

for i in tuple2:
    if tuple2.count(i) > 1:
        print("there is a repeated item")



# solution
"""
unpack a tuple
( ) -> x, y, z, ....

pack 
x, y, z, ... -> ( )
"""

# 2
tuple2 = ('a','b','c')
print(tuple2, type(tuple2))

x, y, z = tuple2
print(x)
print(y)
print(z)


# 3
tuple3 = ('x','y','a','a','b','b','c','c','d','d')
tuple3 = ('a','b','c','c')
for i in tuple3:
    if tuple3.count(i) > 1:
        print("there is a repeated item.")
        break
else:
    print("there is no repeated items.")
# quality of code
# performance


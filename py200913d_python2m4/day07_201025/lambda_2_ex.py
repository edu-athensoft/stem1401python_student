"""
write a program using lambda
to calculate the following expression:

y = ax+b  (line, whereas a != 0)

when x = 10, a = 2, b = 3,  y=?
"""

"""
maths
y = 2x+3

python
y = 2*x + 3
"""

a = 2
b = 3

# y = f(x)
y = lambda x : a*x+b

# call lambda function
x = 10
result = y(10)

print(f"y = {result} when x= 10, a=2 and b=3")



# x = 10
# a = 2
# b = 3
# y = lambda o: a*x+b
#
# result = y(a*x+b)




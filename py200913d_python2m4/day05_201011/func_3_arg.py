"""
variable function arguments
"""

"""
output Good morning, your_friend_name!

friend1 = f1
friend2 = f2
friend3 = f3
friend4 = f4

"""

def greeting(words, name):
    print("{}, {}!".format(words, name))

# 1st
greeting("Good morning", 'f1')

# 2nd
greeting("Good morning", 'f2')

# 3rd
greeting("Good morning", 'f3')

# 4th
greeting("Good morning", 'f4')





"""
# variable parameter
"""

# positional argument
# keyword argument

# f5,f6,f7,f8,f9

# syntax rule
# all keyword args stay after positional argument
# def greeting1(words="Good morning", name):
def greeting1(name, age=15, words="Good morning"):
    # print("{w}, {a}, {n}!".format(w=words, a=age, n=name))
    print("{w}, {a}, {n}!".format(n=name, a=age, w=words ))


greeting1('f5')
greeting1('f6')
greeting1('f7')
greeting1('f8')
greeting1('f9',words='Good evening')

greeting1('f9','Good evening')









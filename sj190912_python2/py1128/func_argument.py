# function argument

def my_func():
    print()

my_func()

# one argument
def my_func2(fname):
    print("Hello {}".format(fname))

my_func2("Puca")
my_func2("Emma")

# two arguments
def adding(x, y):
    result = x + y
    return result

print(adding(1, 2))
print(adding(3, 2))
print(adding(5, 6))

def sum3(a, b, c):
    result = a + b + c
    return result

print(sum3(1,2,3))
print(sum3(10,10,10))
print(sum3(234032,435345,5654654))

# print(sum3(1,2))
# print(sum3(1,2,3,4))

# any number of argument
def get_day_of_week(*day_of_week):
    for i in day_of_week:
        print(i)

get_day_of_week("MON","TUE","WED")

# count the number of argument you passed in
# print out the number
# i.e.

def get_num_of_args(*args):
    pass

num = get_num_of_args("1",'2','3')
print(num)


# default argument
def greeting(username, words="Good morning"):
    print("{}, {}!".format(words, username))

greeting("Emma")
greeting("Eva")
greeting("Adam")
greeting("Emma","Good evening")















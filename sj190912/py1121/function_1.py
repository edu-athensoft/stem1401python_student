# define a simple function


def show_name():
    name = "Joce"
    print('Hello, {}!'.format(name))


# call a function
show_name()
show_name()
show_name()

# define a function with parameters
def show_name2(name):
    print('Hello, {}!'.format(name))

show_name2('David')
show_name2('Amy')
show_name2('Mark')

# return a value or result from a function
# x^2
def square(x):
    result = x ** 2
    return result

a = 78
num = square(a)
print('The square of {} is {}'.format(a, num))
print('The xxxx {} is {}'.format(a, num))
print('The bbbbb of {} is {}'.format(a, num))


def calc(x, y):
    print('Hello, {} {}!'.format(x,y))

calc(10,56)

def adding(x,y):
    return x + y


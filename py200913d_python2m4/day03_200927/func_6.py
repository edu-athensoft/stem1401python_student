"""
function

input   - parameters
output  - returned result/value
"""

# input a number, returns doubled value


def double(x):
    y = 2 * x
    return y

# input x
number = 25
result = double(number)

# print("The result is {}".format(result))


# ex. design a function and use it

# square number
# input a number from your keyboard
# print out its squared value

# i.e.
# input 5
# expected result is 25
# input 6
# is 36


# steps
# 1. make decision whether a function is needed.
# 2. give a name
# 3. write codes  (input/argument/parameter,    return value/output)
# 4. run and test

# Ver 1.
def square(num):
    result = num * num
    return result

# Ver 2.
# float()   str -> floating number
"""
num = float(input("Enter a number: "))
result = square(num)
print(result)
print()
"""

# Ver 3.
# how can we run the function for 10 times
"""
for i in range(10):
    num = float(input("Enter a number: "))
    result = square(num)
    print("Result #{} is {}".format(i+1, result))
    print()
"""

# Ver 4.
# how can we run it for infinite times
while True:
    # task
    num = input("Enter a number [press 'q' or 'quit' to exit]: ")

    if num == 'quit' or num == 'q':
        break
    else:
        num = float(num)

    result = square(num)
    print("Result is {}".format(result))
    print()




